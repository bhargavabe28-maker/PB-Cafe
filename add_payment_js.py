js_content = """document.addEventListener('DOMContentLoaded', () => {
    // Navbar scroll effect
    const navbar = document.querySelector('.navbar');
    window.addEventListener('scroll', () => {
        if (window.scrollY > 50) {
            navbar.classList.add('scrolled');
        } else {
            navbar.classList.remove('scrolled');
        }
    });

    // Smooth scroll for navigation links
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', function (e) {
            e.preventDefault();
            const targetId = this.getAttribute('href');
            if (targetId === '#') return;
            const targetElement = document.querySelector(targetId);
            if (targetElement) {
                targetElement.scrollIntoView({ behavior: 'smooth', block: 'start' });
            }
        });
    });

    // Navigation Tier System
    const categorySelection = document.getElementById('category-selection');
    const itemsView = document.getElementById('items-view');
    const categoryButtons = document.querySelectorAll('.category-card');
    const backBtn = document.getElementById('back-to-categories');
    const currentCategoryTitle = document.getElementById('current-category-title');
    const menuItems = document.querySelectorAll('.menu-item');

    categoryButtons.forEach(btn => {
        btn.addEventListener('click', () => {
            const category = btn.getAttribute('data-category');
            const categoryName = btn.querySelector('h3').textContent;
            
            // Update Title
            currentCategoryTitle.textContent = categoryName;

            // Hide all items first
            menuItems.forEach(item => item.style.display = 'none');
            
            // Show items for this category
            const targetItems = document.querySelectorAll(`.category-${category}`);
            targetItems.forEach(item => item.style.display = 'flex');

            // Switch views
            categorySelection.classList.add('hidden');
            itemsView.classList.remove('hidden');
            
            // Scroll to top of items view
            itemsView.scrollIntoView({ behavior: 'smooth', block: 'start' });
        });
    });

    backBtn.addEventListener('click', () => {
        itemsView.classList.add('hidden');
        categorySelection.classList.remove('hidden');
    });

    // --- Modal Logic ---
    const modal = document.getElementById('order-modal');
    const closeModal = document.querySelector('.close-modal');
    const orderBtns = document.querySelectorAll('.order-btn');
    const modalItemName = document.getElementById('modal-item-name');
    
    // Step 1 Elements
    const step1Details = document.getElementById('step-1-details');
    const typeBtns = document.querySelectorAll('.type-btn');
    const dineInFields = document.getElementById('dine-in-fields');
    const deliveryFields = document.getElementById('delivery-fields');
    const proceedToPayBtn = document.getElementById('proceed-to-pay-btn');
    
    // Step 2 Elements
    const step2Payment = document.getElementById('step-2-payment');
    const paymentAmountText = document.getElementById('payment-amount');
    const payMethodBtns = document.querySelectorAll('.pay-method-btn');
    const cardFields = document.getElementById('card-fields');
    const upiFields = document.getElementById('upi-fields');
    const backToDetailsBtn = document.getElementById('back-to-details-btn');
    const orderForm = document.getElementById('order-form');
    
    // State Elements
    const paymentLoading = document.getElementById('payment-loading');
    const paymentSuccess = document.getElementById('payment-success');
    
    let currentPrice = 0;

    // Reset Modal State
    const resetModal = () => {
        step1Details.classList.remove('hidden');
        step2Payment.classList.add('hidden');
        paymentLoading.classList.add('hidden');
        paymentSuccess.classList.add('hidden');
        if(orderForm) orderForm.reset();
    };

    // Open Modal
    orderBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const itemName = btn.getAttribute('data-item');
            currentPrice = btn.getAttribute('data-price') || 400; // Fallback to 400 if missing
            
            modalItemName.textContent = `Order: ${itemName}`;
            paymentAmountText.textContent = `₹${currentPrice}`;
            proceedToPayBtn.textContent = `Proceed to Payment (₹${currentPrice})`;
            
            resetModal();
            modal.classList.remove('hidden');
        });
    });

    // Close Modal
    const hideModal = () => modal.classList.add('hidden');
    if(closeModal) {
        closeModal.addEventListener('click', hideModal);
    }
    if(modal) {
        modal.addEventListener('click', (e) => {
            if (e.target === modal) hideModal();
        });
    }

    // Toggle Order Type (Dine-in vs Delivery)
    typeBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            typeBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const type = btn.getAttribute('data-type');
            if (type === 'dine-in') {
                dineInFields.classList.remove('hidden');
                document.getElementById('table-number').setAttribute('required', 'true');
                deliveryFields.classList.add('hidden');
                document.getElementById('address').removeAttribute('required');
            } else {
                deliveryFields.classList.remove('hidden');
                document.getElementById('address').setAttribute('required', 'true');
                dineInFields.classList.add('hidden');
                document.getElementById('table-number').removeAttribute('required');
            }
        });
    });

    // Go to Payment Step
    proceedToPayBtn.addEventListener('click', () => {
        // Simple HTML5 validation check
        if(!orderForm.checkValidity()) {
            orderForm.reportValidity();
            return;
        }
        step1Details.classList.add('hidden');
        step2Payment.classList.remove('hidden');
    });

    // Go back to Details Step
    backToDetailsBtn.addEventListener('click', () => {
        step2Payment.classList.add('hidden');
        step1Details.classList.remove('hidden');
    });

    // Toggle Payment Method
    payMethodBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            payMethodBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            const method = btn.getAttribute('data-method');
            if (method === 'card') {
                cardFields.classList.remove('hidden');
                upiFields.classList.add('hidden');
            } else {
                upiFields.classList.remove('hidden');
                cardFields.classList.add('hidden');
            }
        });
    });

    // Submit Payment
    if(orderForm) {
        orderForm.addEventListener('submit', (e) => {
            e.preventDefault();
            
            // Show loading
            step2Payment.classList.add('hidden');
            paymentLoading.classList.remove('hidden');
            
            // Simulate API delay
            setTimeout(() => {
                paymentLoading.classList.add('hidden');
                paymentSuccess.classList.remove('hidden');
                
                // Auto close after 3 seconds
                setTimeout(() => {
                    hideModal();
                }, 3000);
            }, 2000);
        });
    }
});
"""

with open('script.js', 'w', encoding='utf-8') as f:
    f.write(js_content)
print("Updated script.js completely")
