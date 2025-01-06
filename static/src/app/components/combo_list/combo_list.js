/** @odoo-module **/

import { Component, useState, onMounted, onWillUnmount } from "@odoo/owl";

export class ComboList extends Component {
    static template = "l10n_ec_payment_pos.ComboList";
    static props = {
        options: Object,
        defaultOption: String,
        onOptionSelected: Function,
    };

    setup() {
        this.state = useState({
            showOptions: false,
            selectedOption: this.props.defaultOption || [...this.props.options.keys()][0],
            dropdownStyle: { top: "0px", left: "0px", width: "150px" },
        });

        this._onDocumentClick = this._onDocumentClick.bind(this);
    }

    _onSelectOption(key) {
        this.state.selectedOption = key;
        this.props.onOptionSelected(this.state.selectedOption);
        this.state.showOptions = false;
        document.removeEventListener("click", this._onDocumentClick);
    }

    _toggleOptions(event) {
        this.state.showOptions = !this.state.showOptions;
        if (this.state.showOptions) {
            this._setDropdownPosition(event.target);
            document.addEventListener("click", this._onDocumentClick);
        } else {
            document.removeEventListener("click", this._onDocumentClick);
        }
    }

    _setDropdownPosition(target) {
        const rect = target.getBoundingClientRect();
        this.state.dropdownStyle = {
            top: `${rect.bottom + window.scrollY}px`,
            left: `${rect.left + window.scrollX}px`,
            width: `${rect.width+120}px`,
        };
    }

    _onDocumentClick(event) {
        // Verificar si `this.el` está definido antes de llamar a `.contains`
        if (this.el && !this.el.contains(event.target)) {
            this.state.showOptions = false;
            document.removeEventListener("click", this._onDocumentClick);
        }
    }
}
