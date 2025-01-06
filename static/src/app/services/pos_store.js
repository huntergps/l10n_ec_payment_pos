
import { patch } from "@web/core/utils/patch";
import { PosStore } from "@point_of_sale/app/store/pos_store";


patch(PosStore.prototype, {

  async processServerData() {

     await super.processServerData(...arguments);
     this.banks = this.models["res.bank"].getAll();
     this.payment_methods = this.models["pos.payment.method"].getAll();
     this.card_brands = this.models["account.credit.card.brand"].getAll();
     this.card_deadlines = this.models["account.credit.card.deadline"].getAll();
  }

});
