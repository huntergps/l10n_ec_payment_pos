import { PosPayment } from "@point_of_sale/app/models/pos_payment";
import { patch } from "@web/core/utils/patch";
import { serializeDateTime } from "@web/core/l10n/dates";

const { DateTime } = luxon;

patch(PosPayment.prototype, {

  setup(_defaultObj, options) {
      super.setup(...arguments);
      this.transaction_date = serializeDateTime(DateTime.now());
      this.payment_type = this.payment_type || false;
      this.journal_id = this.journal_id || false;
      this.bank_id = this.bank_id || false;
      this.bank_id_code = this.bank_id_code || false;
      this.bank_account_no = this.bank_account_no || false;
      this.bank_account_owner_name = this.bank_account_owner_name || false;
      this.card_type = this.card_type || false;
      this.card_brand_id = this.card_brand_id || false;
      this.card_brand_id_code = this.card_brand_id_code || false;
      this.card_deadline_id = this.card_deadline_id || false;
      this.card_deadline_id_code = this.card_deadline_id_code || false;

 },


  isCashPayment() {
      return this.payment_type=== 'cash' || this.payment_type=== '';
  },

 isBankTransaccionPayment() {
     return this.payment_type=== 'bank';
 },

 isCreditCardPayment() {
     return this.payment_type=== 'card';
 }

});
