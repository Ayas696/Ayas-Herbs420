<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Ayas Herbs 420</title>
    <style>
        :root {
            --primary: #2c3e50;
            --accent: #27ae60;
            --bg: #f8f9fa;
            --text: #333;
        }
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: var(--bg);
            color: var(--text);
        }
        header {
            background-color: var(--primary);
            color: white;
            padding: 20px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 1000;
            box-shadow: 0 2px 10px rgba(0,0,0,0.1);
        }
        .container {
            max-width: 1200px;
            margin: 20px auto;
            padding: 0 20px;
            display: grid;
            grid-template-columns: 2fr 1fr;
            gap: 30px;
        }
        @media (max-width: 768px) {
            .container { grid-template-columns: 1fr; }
        }
        .products-grid {
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
            gap: 20px;
        }
        .product-card {
            background: white;
            border-radius: 8px;
            padding: 15px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            text-align: center;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
        }
        .product-image {
            width: 100%;
            height: 150px;
            background-color: #eaeded;
            border-radius: 6px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 3rem;
            margin-bottom: 15px;
        }
        .product-title {
            font-size: 1.1rem;
            margin: 10px 0;
            font-weight: 600;
        }
        .product-price {
            color: var(--accent);
            font-weight: bold;
            font-size: 1.2rem;
            margin-bottom: 15px;
        }
        .btn {
            background-color: var(--primary);
            color: white;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
            font-weight: 600;
            width: 100%;
            transition: background 0.2s;
        }
        .btn:hover { background-color: #34495e; }
        .btn-whatsapp {
            background-color: var(--accent);
        }
        .btn-whatsapp:hover { background-color: #219150; }
        .cart-panel {
            background: white;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 5px rgba(0,0,0,0.05);
            height: fit-content;
            position: sticky;
            top: 100px;
        }
        .cart-item {
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding: 10px 0;
            border-bottom: 1px solid #eee;
        }
        .cart-total {
            font-size: 1.3rem;
            font-weight: bold;
            margin: 20px 0;
            display: flex;
            justify-content: space-between;
        }
        .bank-details {
            background: #eef9f1;
            border-left: 4px solid var(--accent);
            padding: 12px;
            border-radius: 0 4px 4px 0;
            font-size: 0.9rem;
            margin-bottom: 15px;
        }
    </style>
</head>
<body>

<header>
    <h1>🛍️ Marketplace Storefront</h1>
    <p>Browse items, add to cart, and check out securely via WhatsApp</p>
</header>

<div class="container">
    <!-- Products Catalog Section -->
    <div>
        <h2>Our Catalogue</h2>
        <div class="products-grid" id="products-container"></div>
    </div>

    <!-- Interactive Shopping Cart & Payment Information Section -->
    <div class="cart-panel">
        <h2>Your Shopping Cart</h2>
        <div id="cart-items-container">
            <p style="color: #7f8c8d;">Your cart is empty.</p>
        </div>
        
        <div class="cart-total">
            <span>Total:</span>
            <span id="cart-total-display">R 0.00</span>
        </div>

        <h3>🏦 Payment Instructions</h3>
        <div class="bank-details">
            <strong>Bank Transfer Details:</strong><br>
            Bank Name: Capitec <br>
            Account Holder: <br>
            Account Number: <br>
            Branch Code: <br>
            <em>Reference: Use your name</em>
        </div>
        <p style="font-size: 0.85rem; color: #7f8c8d; margin-bottom: 15px;">
            ℹ️ Clicking check out compiles your invoice receipt and opens WhatsApp. Transfer the money to our account, then reply with your Proof of Payment (PoP) snapshot.
        </p>
        <button class="btn btn-whatsapp" id="checkout-btn" onclick="sendWhatsAppOrder()">Proceed to WhatsApp Checkout 💬</button>
    </div>
</div>

<script>
    // ⚙️ BUSINESS OWNER CONFIGURATION:

    const WHATSAPP_NUMBER = ""

    // 📦 PRODUCT INVENTORY DATABASE:
  
    const products = [
        { id: 1, name: "☕" },
        { id: 2, name: " "🌿" },
        { id: 3, name: ""🧼" },
        { id: 4, name: " "🌡️" },
        { id: 5, name: "
        { id: 6, name: " , 
        { id: 7, name: " ,
        
    ];

    let cart = {};

    // Render store catalog programmatically onto the DOM layout
    function displayProducts() {
        const container = document.getElementById('products-container');
        container.innerHTML = products.map(product => `
            <div class="product-card">
            
                <div class="product-title">${product.name}</div>
                <div class="product-price">R ${product.price.toFixed(2)}</div>
                <button class="btn" onclick="addToCart(${product.id})">Add to Cart</button>
            </div>
        `).join('');
    }

    function addToCart(productId) {
        if (cart[productId]) {
            cart[productId]++;
        } else {
            cart[productId] = 1;
        }
        updateCartUI();
    }

    function changeQuantity(productId, delta) {
        if (!cart[productId]) return;
        cart[productId] += delta;
        if (cart[productId] <= 0) {
            delete cart[productId];
        }
        updateCartUI();
    }

    function updateCartUI() {
        const container = document.getElementById('cart-items-container');
        const totalDisplay = document.getElementById('cart-total-display');
        
        const cartKeys = Object.keys(cart);
        if (cartKeys.length === 0) {
            container.innerHTML = '<p style="color: #7f8c8d;">Your cart is empty.</p>';
            totalDisplay.innerText = "R 0.00";
            return;
        }

        let totalPrice = 0;
        let html = '';

        cartKeys.forEach(id => {
            const product = products.find(p => p.id == id);
            const qty = cart[id];
            const itemTotal = product.price * qty;
            totalPrice += itemTotal;

            html += `
                <div class="cart-item">
                    <div>
                        <div style="font-weight:600;">${product.name}</div>
                        <div style="font-size:0.85rem; color:#7f8c8d;">R ${product.price.toFixed(2)} each</div>
                    </div>
                    <div style="display:flex; align-items:center; gap:8px;">
                        <button onclick="changeQuantity(${id}, -1)" style="padding:2px 6px;">-</button>
                        <span>${qty}</span>
                        <button onclick="changeQuantity(${id}, 1)" style="padding:2px 6px;">+</button>
                        <span style="font-weight:600; margin-left:10px;">R ${itemTotal.toFixed(2)}</span>
                    </div>
                </div>
            `;
        });

        container.innerHTML = html;
        totalDisplay.innerText = `R ${totalPrice.toFixed(2)}`;
    }

    // Compiles items, calculates absolute sums, formatting raw clean text parameters for WhatsApp URL string actions
    function sendWhatsAppOrder() {
        const cartKeys = Object.keys(cart);
        if (cartKeys.length === 0) {
            alert("Your shopping cart is empty! Please add items before checking out.");
            return;
        }

        let textMessage = `👋 Hello! I'd like to place an order:\n\n🛍️ *ORDER RECEIPT:*\n`;
        let totalPrice = 0;

        cartKeys.forEach(id => {
            const product = products.find(p => p.id == id);
            const qty = cart[id];
            const itemTotal = product.price * qty;
            totalPrice += itemTotal;
            textMessage += `• ${product.name} (x${qty}) - R ${itemTotal.toFixed(2)}\n`;
        });

        textMessage += `\n💰 *Total Amount:* R ${totalPrice.toFixed(2)}\n\n`;
        textMessage += `🏦 I am making an EFT payment to your bank account right now and will send my snapshot Proof of Payment (PoP) directly below this message!`;

        // Direct cross-platform web URL string compilation
        const encodedMessage = encodeURIComponent(textMessage);
        const whatsappUrl = `https://wa.me{270640503383}?text=${encodedMessage}`;
        
        // Relocates user focus cleanly to native WhatsApp communication client threads
