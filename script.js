document.addEventListener('DOMContentLoaded', () => {
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

    // Modal Logic
    const modal = document.getElementById('order-modal');
    const closeModal = document.querySelector('.close-modal');
    const orderBtns = document.querySelectorAll('.order-btn');
    const modalItemName = document.getElementById('modal-item-name');
    const typeBtns = document.querySelectorAll('.type-btn');
    const dineInFields = document.getElementById('dine-in-fields');
    const deliveryFields = document.getElementById('delivery-fields');
    const orderForm = document.getElementById('order-form');

    // Open Modal
    orderBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const itemName = btn.getAttribute('data-item');
            modalItemName.textContent = `Order: ${itemName}`;
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

    // Toggle Order Type
    typeBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            // Remove active from all
            typeBtns.forEach(b => b.classList.remove('active'));
            // Add active to clicked
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

    if(orderForm) {
        orderForm.addEventListener('submit', (e) => {
            e.preventDefault();
            alert('Order placed successfully!');
            hideModal();
            orderForm.reset();
        });
    }
});
