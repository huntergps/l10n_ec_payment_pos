import {
    formatFloat, roundDecimals as round_di,
    roundPrecision as round_pr,floatIsZero,
} from "@web/core/utils/numbers";
import { random5Chars, uuidv4, getOnNotified } from "@point_of_sale/utils";
import { _t } from "@web/core/l10n/translation";

import { Component } from "@odoo/owl";
import { usePos } from "@point_of_sale/app/store/pos_hook";
// import { usePos } from "@point_of_sale/app/hooks/pos_hook";
const { DateTime } = luxon;
import { serializeDateTime } from "@web/core/l10n/dates";
import { Dialog } from "@web/core/dialog/dialog";
import { patch } from "@web/core/utils/patch";
// import { PosStore } from "@point_of_sale/app/services/pos_store";
import { PosStore } from "@point_of_sale/app/store/pos_store";
import { TicketScreen } from "@point_of_sale/app/screens/ticket_screen/ticket_screen";
import { PaymentScreen } from "@point_of_sale/app/screens/payment_screen/payment_screen";
import { ActionScreen } from "@point_of_sale/app/screens/action_screen";


patch(PosStore.prototype, {

  listarDiariosNew() {
      return true;
  },


});
