# PB Cafe ☕

PB Cafe is a premium, minimalist web application for a modern urban coffee house. Built to embody an elegant aesthetic with maximum flavor, this platform allows customers to explore a curated menu of artisanal coffee, handcrafted toasts, and signature drinks. It features an integrated ordering system and an administrative dashboard powered by Firebase for seamless order management.

## ✨ Features

- **Modern & Minimalist UI:** A sleek, responsive, and aesthetically pleasing design emphasizing the cafe's urban vibe.
- **Categorized Menu Navigation:** A dynamic 3-tier menu system offering curated selections across **Coffee**, **Toasts**, and **Drinks**.
- **Integrated Ordering System:** Support for both Dine-In and Home Delivery orders.
- **Secure Payment Flow:** Flexible payment processing UI that supports Card and UPI methods, including manual UTR (transaction reference) validation.
- **Firebase Backend:** Real-time data synchronization for storing and retrieving orders using Firebase Firestore.
- **Admin Dashboard:** A secure staff dashboard that enables real-time tracking of pending and completed orders. Includes status updates and duplicate transaction prevention.

## 🛠️ Tech Stack

- **Frontend:** HTML5, CSS3 (Vanilla), JavaScript (ES6)
- **Backend / Database:** Firebase Firestore (Cloud Database)

## 🚀 Getting Started

### Prerequisites

To run this project locally, you don't need any complex build tools. A simple local web server will suffice.

### Installation & Setup

1. **Clone or Download the repository:**
   Ensure you have the full project directory including the `assets`, `index.html`, `style.css`, and `script.js`.

2. **Firebase Setup:**
   - The project is pre-configured with a Firebase project. 
   - If setting up a new environment, update the `firebaseConfig` object located in `index.html` with your own project credentials. Ensure your Firestore Database has the proper security rules.

3. **Run the application:**
   - Start a local development server (e.g. Live Server in VS Code, or `python -m http.server`) in the project directory.
   - Or simply open `index.html` directly in your browser.

## 🔐 Admin Access

To manage orders and view the dashboard, use the Admin login modal accessed via the "Admin" link in the navigation bar.

- **Admin ID:** `Admin0327`
- **Password:** `PB0327`

*(Note: These are hardcoded credentials for demonstration purposes.)*

## 🎨 Design Philosophy

"People & Beans" - Our digital space is designed to strip away the noise of the city, much like our physical cafe. We focused on a user-centric digital experience, ensuring that every interaction—from browsing the menu to confirming an order—feels as smooth and carefully crafted as our signature beverages.

## 📄 License

&copy; 2026 PB Cafe. All rights reserved.
