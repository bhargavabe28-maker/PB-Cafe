import re

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

coffee_menu_html = """<!-- Signature Coffee -->
                    <!-- Hot Coffee (Premium) -->
                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1541167760496-1628856ab772?auto=format&fit=crop&w=400&q=80" alt="The Araku Signature Latte" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>The Araku Signature Latte</h4>
                            <p>Smooth, locally sourced, and naturally sweet.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹450</span>
                                <button class="order-btn" data-item="The Araku Signature Latte">Order It</button>
                            </div>
                        </div>
                    </div>
                    
                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1550583724-b2692b85b150?auto=format&fit=crop&w=400&q=80" alt="Banjara Hills Dark Roast" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Banjara Hills Dark Roast</h4>
                            <p>A bold, intense cup perfect for the city's morning rush.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹350</span>
                                <button class="order-btn" data-item="Banjara Hills Dark Roast">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1578314675249-a694eb286151?auto=format&fit=crop&w=400&q=80" alt="Velvet Flat White" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Velvet Flat White</h4>
                            <p>A silky, high-end version of a latte with a stronger espresso hit.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹420</span>
                                <button class="order-btn" data-item="Velvet Flat White">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1534687941688-651ccaafbff8?auto=format&fit=crop&w=400&q=80" alt="Malabar Spice Cappuccino" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Malabar Spice Cappuccino</h4>
                            <p>Using Monsoon Malabar beans with a hint of local cinnamon.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹390</span>
                                <button class="order-btn" data-item="Malabar Spice Cappuccino">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1497935586351-b67a49e012bf?auto=format&fit=crop&w=400&q=80" alt="Artisanal Pour-Over" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Artisanal Pour-Over</h4>
                            <p>For the true coffee nerd; features a rotating single-origin bean.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹480</span>
                                <button class="order-btn" data-item="Artisanal Pour-Over">Order It</button>
                            </div>
                        </div>
                    </div>

                    <!-- Cold Coffee & Drinks -->
                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1461023058943-07fcbe16d735?auto=format&fit=crop&w=400&q=80" alt="Midnight Cold Brew" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Midnight Cold Brew</h4>
                            <p>Steeped for 18 hours for a smooth, chocolatey finish.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹400</span>
                                <button class="order-btn" data-item="Midnight Cold Brew">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1572490122747-3968b75cc699?auto=format&fit=crop&w=400&q=80" alt="Hyderabad Hazelnut Frappé" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Hyderabad Hazelnut Frappé</h4>
                            <p>A crowd favorite—rich, icy, and nutty.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹450</span>
                                <button class="order-btn" data-item="Hyderabad Hazelnut Frappé">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1517701550927-30cf4ba1dba1?auto=format&fit=crop&w=400&q=80" alt="Iced Sea Salt Mocha" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Iced Sea Salt Mocha</h4>
                            <p>A trendy mix of dark chocolate, espresso, and a pinch of salt.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹460</span>
                                <button class="order-btn" data-item="Iced Sea Salt Mocha">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1517701604599-bb29b565090c?auto=format&fit=crop&w=400&q=80" alt="The Jubilee Iced Americano" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>The "Jubilee" Iced Americano</h4>
                            <p>A refreshing, clean black coffee over crystal ice.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹350</span>
                                <button class="order-btn" data-item="The Jubilee Iced Americano">Order It</button>
                            </div>
                        </div>
                    </div>

                    <div class="menu-item category-coffee">
                        <img src="https://images.unsplash.com/photo-1546487201-948fcd6d0152?auto=format&fit=crop&w=400&q=80" alt="Coconut Milk Brew" class="menu-item-img">
                        <div class="menu-item-content">
                            <h4>Coconut Milk Brew</h4>
                            <p>A vegan-friendly, creamy tropical twist on iced coffee.</p>
                            <div class="menu-item-footer">
                                <span class="price">₹430</span>
                                <button class="order-btn" data-item="Coconut Milk Brew">Order It</button>
                            </div>
                        </div>
                    </div>
"""

pattern = re.compile(r'<!-- Signature Coffee -->.*?(?=<!-- Artisanal Toasts -->)', re.DOTALL)
new_content = pattern.sub(coffee_menu_html + '                    ', content)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(new_content)
    
print("Updated successfully")
