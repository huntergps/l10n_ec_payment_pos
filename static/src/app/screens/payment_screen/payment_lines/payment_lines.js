import { patch } from "@web/core/utils/patch";
import { PaymentScreenPaymentLines } from "@point_of_sale/app/screens/payment_screen/payment_lines/payment_lines";
import { ComboList } from "@l10n_ec_payment_pos/app/components/combo_list/combo_list";

patch(PaymentScreenPaymentLines.prototype, {
    setup() {
        super.setup(...arguments);
    },

    _onPaymentRefNoChange(line, value) {
        line.payment_ref_no = value;
    },

    _onTransactionDateChange(line, value) {
        line.transaction_date = value;
    },

    _onJournalIdChange(line, value) {
      console.log(line.journal_id);
        // line.journal_id = value;
        console.log('line.bank_id: ',line.bank_id);
    },


    _onBankAccountNoChange(line, value) {
        line.bank_account_no = value;
    },

    _onBankIdChange(line, value) {
        line.bank_id_code = value;
        console.log('line.journal_id: ',line.journal_id);
        console.log('line.bank_id: ',line.bank_id);
        console.log('line.bank_id_code: ',line.bank_id_code);
    },





    _onBankAccountOwnerNameChange(line, value) {
        line.bank_account_owner_name = value;
    },

    _onTransactionTypeChange(line, value) {
        line.transaction_type = value;
    },

    _onCardTypeChange(line, value) {
        line.card_type = value;
    },

});
