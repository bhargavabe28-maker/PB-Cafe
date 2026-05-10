import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

menu_replacement = """        <div class="menu-container">
            <!-- Tier 1: Category Selection -->
            <div id="category-selection" class="category-selection">
                <button class="category-card" data-category="coffee" style="background-image: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)), url('assets/images/coffee.png');">
                    <h3>Coffee</h3>
                </button>
                <button class="category-card" data-category="toasts" style="background-image: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)), url('assets/images/toast.png');">
                    <h3>Toasts</h3>
                </button>
                <button class="category-card" data-category="drinks" style="background-image: linear-gradient(to top, rgba(0,0,0,0.8), rgba(0,0,0,0.2)), url('assets/images/drink.png');">
                    <h3>Drinks</h3>
                </button>
            </div>

            <!-- Tier 2: Items View -->
            <div id="items-view" class="items-view hidden">
                <div class="items-header">
                    <button id="back-to-categories" class="back-btn">&larr; Back to Categories</button>
                    <h3 id="current-category-title" class="category-title">Category</h3>
                </div>
                
                <div class="menu-grid" id="menu-grid">
                    <!-- Signature Coffee -->
                    <div class="menu-item category-coffee">
                        <img src="assets/images/coffee.png" alt="Charcoal Vanilla Latte" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Charcoal Vanilla Latte</h4>
                            <p>Our signature espresso with activated charcoal and house-made vanilla bean syrup.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹450</span>
                                <button class="order-btn" data-item="Charcoal Vanilla Latte">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-coffee">
                        <img src="assets/images/coffee.png" alt="Oak-Aged Cold Brew" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Oak-Aged Cold Brew</h4>
                            <p>Steeped for 24 hours in oak barrels, smooth and woody.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹390</span>
                                <button class="order-btn" data-item="Oak-Aged Cold Brew">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-coffee">
                        <img src="assets/images/coffee.png" alt="Classic Cortado" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Classic Cortado</h4>
                            <p>A perfect balance of equal parts espresso and steamed milk.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹330</span>
                                <button class="order-btn" data-item="Classic Cortado">Order It</button>
                            </div>
                        </div>
                    </div>

                    <!-- Artisanal Toasts -->
                    <div class="menu-item category-toasts">
                        <img src="assets/images/toast.png" alt="Avocado & Chili Crunch" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Avocado & Chili Crunch</h4>
                            <p>Smashed avocado, house chili crisp, sea salt, artisan sourdough.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹350</span>
                                <button class="order-btn" data-item="Avocado & Chili Crunch">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-toasts">
                        <img src="assets/images/toast.png" alt="Ricotta & Honey Fig" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Ricotta & Honey Fig</h4>
                            <p>Whipped ricotta, seasonal figs, hot honey drizzle, crusts.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹380</span>
                                <button class="order-btn" data-item="Ricotta & Honey Fig">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-toasts">
                        <img src="assets/images/toast.png" alt="Smoked Salmon" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Smoked Salmon</h4>
                            <p>Cured salmon, cream cheese, capers, dill, on rye.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹420</span>
                                <button class="order-btn" data-item="Smoked Salmon">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-toasts">
                        <img src="assets/images/toast.png" alt="Heirloom Tomato & Pesto" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Heirloom Tomato & Pesto</h4>
                            <p>Sliced heirloom tomatoes, house-made basil pesto, and burrata on rustic bread.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹400</span>
                                <button class="order-btn" data-item="Heirloom Tomato & Pesto">Order It</button>
                            </div>
                        </div>
                    </div>

                    <!-- Craft Drinks -->
                    <div class="menu-item category-drinks">
                        <img src="assets/images/drink.png" alt="Matcha-Mingle" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Matcha-Mingle</h4>
                            <p>Ceremonial-grade matcha with hints of white chocolate, served over ice.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹490</span>
                                <button class="order-btn" data-item="Matcha-Mingle">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-drinks">
                        <img src="assets/images/drink.png" alt="Chai-Lavender Elixir" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Chai-Lavender Elixir</h4>
                            <p>House-made spiced chai blend with a delicate lavender finish, warm or cold.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹410</span>
                                <button class="order-btn" data-item="Chai-Lavender Elixir">Order It</button>
                            </div>
                        </div>
                    </div>
                    <div class="menu-item category-drinks">
                        <img src="assets/images/drink.png" alt="Hibiscus Rose Cooler" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Hibiscus Rose Cooler</h4>
                            <p>Chilled hibiscus tea with notes of rosehip and a mint garnish.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹370</span>
                                <button class="order-btn" data-item="Hibiscus Rose Cooler">Order It</button>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>"""

modal_content = """
    <!-- Order Modal -->
    <div id="order-modal" class="modal hidden">
        <div class="modal-content">
            <button class="close-modal">&times;</button>
            <h2 id="modal-item-name">Order Item</h2>
            
            <div class="order-type-selection">
                <button class="type-btn active" data-type="dine-in">Dine-In</button>
                <button class="type-btn" data-type="delivery">Home Delivery</button>
            </div>
            
            <form id="order-form">
                <div id="dine-in-fields" class="form-group">
                    <label for="table-number">Table Number</label>
                    <input type="number" id="table-number" placeholder="Enter your table number" required>
                </div>
                
                <div id="delivery-fields" class="form-group hidden">
                    <label for="address">Delivery Address</label>
                    <textarea id="address" placeholder="Enter your full delivery address" rows="3"></textarea>
                </div>
                
                <button type="submit" class="confirm-order-btn">Confirm Order</button>
            </form>
        </div>
    </div>
"""

pattern = re.compile(r'<div class="menu-container">.*?(?=</section>)', re.DOTALL)
content = pattern.sub(menu_replacement + '\n    ', content)

content = content.replace('<script src="script.js"></script>', modal_content + '\n    <script src="script.js"></script>')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated index.html successfully.")
