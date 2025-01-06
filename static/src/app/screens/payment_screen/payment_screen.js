import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { patch } from "@web/core/utils/patch";
import { useService } from "@web/core/utils/hooks";
import { ComboList } from "@l10n_ec_payment_pos/app/components/combo_list/combo_list";

patch(PaymentScreen.prototype, {
     setup() {
         super.setup(...arguments);
         this.JournalComboList = ComboList;
         this.BankComboList = ComboList;
         this.CardBrandComboList = ComboList;
         this.CardDeadLineComboList = ComboList;
     },

    deletePaymentLine(uuid) {
      const line = this.paymentLines.find((line) => line.uuid === uuid);
      line.journal_ids_allowed=[];
      super.deletePaymentLine(uuid);

    },
    async addNewPaymentLine(paymentMethod) {
        const result = await super.addNewPaymentLine(paymentMethod);
        if (result && this.selectedPaymentLine) {
          this.selectedPaymentLine.payment_type = paymentMethod.payment_type;
          this.selectedPaymentLine.transaction_type = '';
            if (paymentMethod.serialized_allowed_journals) {
                this.selectedPaymentLine.journalOptions = new Map(
                    paymentMethod.serialized_allowed_journals
                        .filter(journal => journal.id && journal.name)  // Filtrar entradas válidas
                        .map(journal => [String(journal.id), journal.name])  // Convertir ID a string
                );
                this.selectedPaymentLine.journal_ids_allowed = paymentMethod.serialized_allowed_journals;
                this.selectedPaymentLine.journal_id = String(paymentMethod.serialized_allowed_journals?.[0]?.id || '');
                this.selectedPaymentLine.JournalComboList = this.JournalComboList;
                this.selectedPaymentLine.showJournalOptions = false;  // Inicializar el estado del desplegable
            }
            if (this.pos.banks) {
                this.selectedPaymentLine.bankOptions = new Map(
                    this.pos.banks
                        .filter(bank => bank.id && bank.name)  // Filtrar entradas válidas
                        .map(bank => [String(bank.id), bank.name])  // Convertir ID a string
                );
                this.selectedPaymentLine.bank_id = String(this.pos.banks?.[0]?.id || '');
                this.selectedPaymentLine.BankComboList = this.BankComboList;
                this.selectedPaymentLine.showBankOptions = false;  // Inicializar el estado del desplegable
            }
            if (this.pos.card_brands) {
                this.selectedPaymentLine.cardBrandOptions = new Map(
                    this.pos.card_brands
                        .filter(cardBrand => cardBrand.id && cardBrand.name)  // Filtrar entradas válidas
                        .map(cardBrand => [String(cardBrand.id), cardBrand.name])  // Convertir ID a string
                );
                this.selectedPaymentLine.card_brand_id = String(this.pos.card_brands?.[0]?.id || '');
                this.selectedPaymentLine.CardBrandComboList = this.CardBrandComboList;
                this.selectedPaymentLine.showCardBrandOptions = false;  // Inicializar el estado del desplegable
            }

            if (this.pos.card_deadlines) {
                this.selectedPaymentLine.cardDeadlineOptions = new Map(
                    this.pos.card_deadlines
                        .filter(cardDeadline => cardDeadline.id && cardDeadline.name)  // Filtrar entradas válidas
                        .map(cardDeadline => [String(cardDeadline.id), cardDeadline.name])  // Convertir ID a string
                );
                this.selectedPaymentLine.card_deadline_id = String(this.pos.card_deadlines?.[0]?.id || '');
                this.selectedPaymentLine.CardDeadlineComboList = this.CardDeadlineComboList;
                this.selectedPaymentLine.showCardDeadlineOptions = false;  // Inicializar el estado del desplegable
            }

        }
        console.log('this.selectedPaymentLine.payment_type  : ',this.selectedPaymentLine.payment_type);
        return result;
    },


});
