from pyscript import display, document

# jan cabading

def order(e):
    # prices (php)
    aglio_olio_price = 280
    pesto_price = 250
    truffle_pasta_price = 300

    # checkbox status
    oredered_aglio_olio = float(document.getElementById("aglio_olio").checked)
    ordered_pesto = float(document.getElementById("pesto").checked)
    ordered_truffle_pasta = float(document.getElementById("truffle_pasta").checked)

    # calculate subtotal
    subtotal = (
        (aglio_olio_price * oredered_aglio_olio) +
        (pesto_price * ordered_pesto) +
        (truffle_pasta_price * ordered_truffle_pasta)
    )

    # 12%
    vat = subtotal * 0.12

    # total
    total = subtotal + vat

    # update currency
    document.getElementById("subtotal").innerText = f"₱{subtotal}"
    document.getElementById("vat").innerText = f"₱{vat}"
    document.getElementById("total").innerText = f"₱{total}"