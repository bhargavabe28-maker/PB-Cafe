import re
import random

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add random prices to buttons
def add_price(match):
    item_name = match.group(1)
    price = random.choice([350, 390, 420, 450, 490, 520])
    return f'<button class="order-btn" data-item="{item_name}" data-price="{price}">Order It</button>'

content = re.sub(r'<button class="order-btn" data-item="(.*?)">Order It</button>', add_price, content)

# Replace Modal
old_modal_pattern = re.compile(r'<!-- Order Modal -->.*?</div>\s*</div>\s*<script src="script\.js"></script>', re.DOTALL)

new_modal = """<!-- Order Modal -->
    <div id="order-modal" class="modal hidden">
        <div class="modal-content">
            <button class="close-modal">&times;</button>
            <h2 id="modal-item-name">Order Item</h2>
            
            <form id="order-form">
                <!-- Step 1: Details -->
                <div id="step-1-details">
                    <div class="order-type-selection">
                        <button class="type-btn active" data-type="dine-in">Dine-In</button>
                        <button class="type-btn" data-type="delivery">Home Delivery</button>
                    </div>
                    
                    <div id="dine-in-fields" class="form-group">
                        <label for="table-number">Table Number</label>
                        <input type="number" id="table-number" placeholder="Enter your table number" required>
                    </div>
                    
                    <div id="delivery-fields" class="form-group hidden">
                        <label for="address">Delivery Address</label>
                        <textarea id="address" placeholder="Enter your full delivery address" rows="3"></textarea>
                    </div>
                    
                    <button type="button" id="proceed-to-pay-btn" class="confirm-order-btn">Proceed to Payment</button>
                </div>

                <!-- Step 2: Payment -->
                <div id="step-2-payment" class="hidden">
                    <h3 class="payment-title">Amount to Pay: <span id="payment-amount">₹0</span></h3>
                    
                    <div class="payment-methods">
                        <button type="button" class="pay-method-btn active" data-method="card">Card</button>
                        <button type="button" class="pay-method-btn" data-method="upi">UPI</button>
                    </div>

                    <div id="card-fields" class="form-group">
                        <label>Card Number</label>
                        <input type="text" placeholder="XXXX XXXX XXXX XXXX">
                        <div style="display:flex; gap:1rem; margin-top:0.5rem;">
                            <input type="text" placeholder="MM/YY" style="flex:1;">
                            <input type="text" placeholder="CVV" style="flex:1;">
                        </div>
                    </div>

                    <div id="upi-fields" class="form-group hidden">
                        <label>UPI ID</label>
                        <input type="text" placeholder="username@upi">
                    </div>

                    <button type="submit" id="final-pay-btn" class="confirm-order-btn pay-submit-btn">Pay Now</button>
                    <button type="button" id="back-to-details-btn" class="back-link-btn">&larr; Back to Details</button>
                </div>
                
                <!-- Loading State -->
                <div id="payment-loading" class="payment-loading hidden">
                    <div class="spinner"></div>
                    <p>Processing Payment...</p>
                </div>
                
                <!-- Success State -->
                <div id="payment-success" class="payment-success hidden">
                    <div class="success-icon">✓</div>
                    <h3>Payment Successful!</h3>
                    <p>Your order is being prepared.</p>
                </div>
            </form>
        </div>
    </div>

    <script src="script.js"></script>"""

content = old_modal_pattern.sub(new_modal, content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)
print("Added payment step to HTML.")
