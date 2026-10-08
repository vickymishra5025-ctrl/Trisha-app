import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Trisha - Official Brand App",
    page_icon="✨",
    layout="centered"
)

# Custom Styling (CSS)
st.markdown("""
    <style>
    .main-title {
        font-size: 38px;
        font-weight: bold;
        color: #d63384;
        text-align: center;
        margin-bottom: 0px;
    }
    .subtitle {
        font-size: 16px;
        color: #6c757d;
        text-align: center;
        margin-bottom: 30px;
    }
    .product-card {
        background-color: #f8f9fa;
        padding: 20px;
        border-radius: 10px;
        border: 1px solid #dee2e6;
        margin-bottom: 15px;
    }
    </style>
""", unsafe_allow_html=True)

# App Header
st.markdown('<p class="main-title">✨ TRISHA ✨</p>', unsafe_allow_html=True)
st.markdown('<p class="subtitle">Elegance & Style Redefined</p>', unsafe_allow_html=True)

# Sidebar Navigation
menu = st.sidebar.selectbox("Navigation", ["Home", "Shop Collection", "Cart", "Contact Us"])

# Products Data
products = {
    "Ethnic Wear": [
        {"name": "Trisha Designer Kurti", "price": "₹2,499", "desc": "Pure cotton embroidered kurti."},
        {"name": "Royal Silk Saree", "price": "₹5,999", "desc": "Traditional festive wear saree."}
    ],
    "Accessories": [
        {"name": "Trisha Gold Plated Jhumkas", "price": "₹899", "desc": "Classic traditional earrings."},
        {"name": "Chic Handbag", "price": "₹1,799", "desc": "Premium leather everyday bag."}
    ]
}

if menu == "Home":
    st.image("https://images.unsplash.com/photo-1441986300917-64674bd600d8?auto=format&fit=crop&w=800&q=80", use_container_width=True)
    st.subheader("Welcome to Trisha World! 💖")
    st.write("Yahan aapko milti hai sabse behtareen quality aur latest trends. Apni pasandida category choose karne ke liye sidebar mein **'Shop Collection'** par click karein.")
    
    st.markdown("---")
    st.info("🔥 **Special Offer:** Pehle order par paayein 15% ka discount! Use code: **TRISHA15**")

elif menu == "Shop Collection":
    st.header("🛍️ Trisha's Exclusive Collection")
    
    category = st.selectbox("Category Chuniye:", list(products.keys()))
    
    st.markdown(f"### {category}")
    
    for item in products[category]:
        st.markdown(f"""
            <div class="product-card">
                <h4>{item['name']}</h4>
                <p>{item['desc']}</p>
                <b>Price: {item['price']}</b>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"Add to Cart - {item['name']}", key=item['name']):
            if 'cart' not in st.session_state:
                st.session_state.cart = []
            st.session_state.cart.append(item)
            st.success(f"{item['name']} aapke cart mein add ho gaya hai! 🎉")

elif menu == "Cart":
    st.header("🛒 Aapka Shopping Cart")
    
    if 'cart' not in st.session_state or not st.session_state.cart:
        st.warning("Aapka cart khali hai!")
    else:
        total = 0
        for idx, cart_item in enumerate(st.session_state.cart):
            st.write(f"{idx+1}. **{cart_item['name']}** — {cart_item['price']}")
            price_val = int(cart_item['price'].replace('₹', '').replace(',', ''))
            total += price_val
        
        st.markdown(f"### Total Amount: ₹{total}")
        if st.button("Proceed to Checkout"):
            st.success("Order successfully place ho gaya hai! Thank you for shopping with Trisha. 💖")
            st.session_state.cart = []

elif menu == "Contact Us":
    st.header("📞 Humse Sampark Karein")
    
    # Brand Contact Details Added Here
    st.success("Aap humein neeche diye gaye madhyamo se contact kar sakte hain:")
    st.markdown("📱 **WhatsApp / Call:** +91 8708228400")
    st.markdown("📧 **Email ID:** support@trishabrand.com")
    
    st.markdown("---")
    st.write("Ya fir aap apna message yahan bhej sakte hain:")
    
    with st.form("contact_form"):
        name = st.text_input("Aapka Naam")
        phone = st.text_input("Aapka Phone Number")
        message = st.text_input("Aapka Message")
        submit = st.form_submit_button("Bhejein")
        
        if submit:
            st.success(f"Shukriya {name}! Aapka message hum tak pahunch gaya hai, hum jald hi 8708228400 par aapse sampark karenge.")
  
