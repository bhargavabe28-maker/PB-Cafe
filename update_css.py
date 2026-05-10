with open('style.css', 'a', encoding='utf-8') as f:
    f.write("""
/* ------------------------------------- */
/* TIER 1: CATEGORY SELECTION */
/* ------------------------------------- */
.category-selection {
    display: flex;
    flex-direction: column;
    gap: 2rem;
    max-width: 800px;
    margin: 0 auto;
}

@media (min-width: 768px) {
    .category-selection {
        flex-direction: row;
        max-width: 1200px;
    }
}

.category-card {
    flex: 1;
    height: 300px;
    border-radius: 20px;
    border: none;
    background-size: cover;
    background-position: center;
    position: relative;
    cursor: pointer;
    overflow: hidden;
    transition: transform 0.3s cubic-bezier(0.25, 0.8, 0.25, 1), box-shadow 0.3s ease;
    box-shadow: 0 10px 30px rgba(0, 0, 0, 0.1);
    display: flex;
    align-items: center;
    justify-content: center;
}

.category-card:hover {
    transform: translateY(-10px);
    box-shadow: 0 15px 40px rgba(0, 0, 0, 0.2);
}

.category-card h3 {
    color: var(--white);
    font-size: 2.5rem;
    font-family: var(--font-serif);
    z-index: 2;
    position: relative;
    letter-spacing: 1px;
}

/* ------------------------------------- */
/* TIER 2: ITEMS VIEW */
/* ------------------------------------- */
.items-view {
    animation: fadeUp 0.5s ease;
}

.hidden {
    display: none !important;
}

.items-header {
    display: flex;
    flex-direction: column;
    align-items: center;
    margin-bottom: 3rem;
}

.back-btn {
    background: none;
    border: none;
    color: var(--charcoal-light);
    font-size: 1rem;
    cursor: pointer;
    font-family: var(--font-sans);
    margin-bottom: 1rem;
    transition: color 0.3s;
}

.back-btn:hover {
    color: var(--warm-oak);
}

.category-title {
    font-family: var(--font-serif);
    font-size: 2.5rem;
    color: var(--charcoal-grey);
}

/* Menu Item Updates */
.order-btn {
    background-color: var(--charcoal-grey);
    color: var(--white);
    border: none;
    padding: 0.6rem 1.5rem;
    border-radius: 8px;
    font-family: var(--font-sans);
    font-weight: 600;
    cursor: pointer;
    transition: background-color 0.3s;
}

.order-btn:hover {
    background-color: var(--warm-oak);
}

/* ------------------------------------- */
/* TIER 3: MODAL */
/* ------------------------------------- */
.modal {
    position: fixed;
    top: 0;
    left: 0;
    width: 100%;
    height: 100%;
    background: rgba(0, 0, 0, 0.6);
    backdrop-filter: blur(5px);
    -webkit-backdrop-filter: blur(5px);
    z-index: 2000;
    display: flex;
    align-items: center;
    justify-content: center;
}

.modal-content {
    background: var(--white);
    width: 90%;
    max-width: 500px;
    border-radius: 16px;
    padding: 2.5rem;
    position: relative;
    box-shadow: 0 20px 50px rgba(0,0,0,0.2);
    animation: fadeUp 0.4s cubic-bezier(0.25, 0.8, 0.25, 1);
}

.close-modal {
    position: absolute;
    top: 15px;
    right: 20px;
    background: none;
    border: none;
    font-size: 2rem;
    cursor: pointer;
    color: var(--charcoal-light);
}

.modal-content h2 {
    font-family: var(--font-serif);
    margin-bottom: 1.5rem;
    color: var(--charcoal-grey);
}

.order-type-selection {
    display: flex;
    gap: 1rem;
    margin-bottom: 2rem;
}

.type-btn {
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

.type-btn.active, .type-btn:hover {
    background: var(--charcoal-grey);
    color: var(--white);
}

.form-group {
    margin-bottom: 1.5rem;
    display: flex;
    flex-direction: column;
    gap: 0.5rem;
}

.form-group label {
    font-weight: 600;
    color: var(--charcoal-grey);
}

.form-group input, .form-group textarea {
    padding: 0.8rem;
    border: 1px solid #ccc;
    border-radius: 8px;
    font-family: var(--font-sans);
}

.confirm-order-btn {
    width: 100%;
    padding: 1rem;
    background-color: var(--warm-oak);
    color: var(--white);
    border: none;
    border-radius: 8px;
    font-size: 1.1rem;
    font-weight: 700;
    cursor: pointer;
    transition: background-color 0.3s;
    margin-top: 1rem;
}

.confirm-order-btn:hover {
    background-color: var(--warm-oak-light);
}
""")
print("CSS appended successfully")
