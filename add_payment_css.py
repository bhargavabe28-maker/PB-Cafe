with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* ------------------------------------- */
/* PAYMENT STEP STYLES */
/* ------------------------------------- */
.payment-title {
    font-family: var(--font-serif);
    color: var(--charcoal-grey);
    text-align: center;
    margin-bottom: 1.5rem;
    font-size: 1.4rem;
}

#payment-amount {
    color: var(--warm-oak);
    font-weight: 700;
}

.payment-methods {
    display: flex;
    gap: 1rem;
    margin-bottom: 1.5rem;
}

.pay-method-btn {
    flex: 1;
    padding: 0.8rem;
    border: 1px solid var(--charcoal-grey);
    background: transparent;
    border-radius: 8px;
    cursor: pointer;
    font-family: var(--font-sans);
    font-weight: 600;
    color: var(--charcoal-grey);
    transition: all 0.3s;
}

.pay-method-btn.active, .pay-method-btn:hover {
    background: var(--charcoal-grey);
    color: var(--white);
}

.back-link-btn {
    width: 100%;
    background: none;
    border: none;
    color: var(--charcoal-light);
    font-family: var(--font-sans);
    font-weight: 600;
    margin-top: 1rem;
    cursor: pointer;
    text-align: center;
    transition: color 0.3s;
}

.back-link-btn:hover {
    color: var(--warm-oak);
}

.payment-loading, .payment-success {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    padding: 3rem 0;
    text-align: center;
}

.payment-success h3 {
    font-family: var(--font-serif);
    color: var(--charcoal-grey);
    margin: 1rem 0 0.5rem;
}

.success-icon {
    width: 60px;
    height: 60px;
    background: var(--warm-oak);
    color: var(--white);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 2rem;
    margin-bottom: 1rem;
}

.spinner {
    width: 50px;
    height: 50px;
    border: 5px solid rgba(45, 45, 45, 0.1);
    border-top-color: var(--warm-oak);
    border-radius: 50%;
    animation: spin 1s linear infinite;
    margin-bottom: 1rem;
}

@keyframes spin {
    to { transform: rotate(360deg); }
}
""")
print("Payment CSS added.")
