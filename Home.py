import streamlit as st

def landing_page():
    st.markdown("""
    <style>
    .stApp {
        background-color: #121212;
        color: #e0e0e0;
    }

    .main-header {
        color: rgb(255, 75, 75);
        font-size: 3.5rem;
        font-weight: bold;
        text-align: center;
        margin-bottom: 30px;
        text-shadow: 0 0 15px rgba(255, 75, 75, 0.6);
    }
    
    .subheader {
        color: rgba(255, 75, 75, 0.7);
        text-align: center;
        font-size: 1.5rem;
        margin-bottom: 40px;
    }
    
    .feature-card {
        background-color: #1E1E1E;
        border-radius: 20px;
        padding: 30px;
        text-align: center;
        box-shadow: 0 8px 15px rgba(0,0,0,0.6);
        border: 1px solid #333;
        transition: transform 0.4s ease, box-shadow 0.4s ease;
        margin: 10px;
    }
    
    .feature-card:hover {
        transform: scale(1.07);
        box-shadow: 0 12px 25px rgba(255, 75, 75, 0.4);
    }
    
    .feature-card h3 {
        color: rgb(255, 75, 75);
        margin-bottom: 15px;
        font-size: 1.5rem;
    }
    
    .feature-card p {
        color: #B0BEC5;
        line-height: 1.6;
    }
    
    .cta-button {
        display: block;
        width: 300px;
        margin: 40px auto;
        padding: 15px;
        background-color: rgba(255, 75, 75, 0.8);
        color: #fff;
        border-radius: 12px;
        text-align: center;
        font-size: 1.3rem;
        text-decoration: none;
        font-weight: bold;
        transition: all 0.4s ease;
        box-shadow: 0 6px 12px rgba(255, 75, 75, 0.5);
    }
    
    .cta-button:hover {
        background-color: rgb(255, 75, 75);
        transform: scale(1.05);
        box-shadow: 0 8px 15px rgba(255, 75, 75, 0.7);
    }
    
    h2 {
        color: rgb(255, 75, 75);
        text-align: center;
        margin-top: 50px;
        margin-bottom: 30px;
        border-bottom: 3px solid rgb(255, 75, 75);
        padding-bottom: 15px;
        letter-spacing: 1px;
    }
    .desc{
        color: #FFFF00;
    }
    p{
        color : white;
        font-size: 50.5rem
    }

    </style>
    """, unsafe_allow_html=True)
    st.markdown(
        """
        <style>
            .main-header {
                font-size: 6vw !important; /* Responsive font size */
                text-align: center;
                font-weight: bold;
                color: #2E3A59;
            }

            @media screen and (max-width: 768px) {
                .main-header {
                    font-size: 9vw !important; /* Larger font on smaller screens */
                }
            }

            @media screen and (max-width: 480px) {
                .main-header {
                    font-size: 13vw !important; /* Even larger font for mobile screens */
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="main-header">FinTrack: Smart Expense Management</h1>',
                unsafe_allow_html=True)

    st.markdown('<p class="subheader">AI-Powered Financial Tracking and Insights</p>',
                unsafe_allow_html=True)

    st.markdown(
        """
        <style>
        .intro-container {
            display: flex;
            align-items: center;
            justify-content: space-between;
            background-color: #1E1E1E;
            border-radius: 15px;
            padding: 25px;
            box-shadow: 0 6px 12px rgba(0,0,0,0.5);
            border: 1px solid #333;
            width: 100%;
            margin-bottom: 20px;
        }

        .intro-text {
            flex: 1;
            color: #e0e0e0;
            font-size: 18px;
            text-align: left;
            line-height: 1.6;
            padding-right: 20px;
        }

        .intro-image img {
            width: 350px;
            height: auto;
            border-radius: 10px;
           
        }

        @media (max-width: 768px) {
            .intro-container {
                flex-direction: column;
                text-align: center;
            }

            .intro-text {
                padding-right: 0;
                text-align: center;
            }

            .intro-image img {
                width: 100%;
            }
        }
        </style>

        <div class="intro-container">
            <div class="intro-image">
                <img src="https://github.com/deringirish/DevOpsTesing/blob/main/receitp_scanner.png?raw=true" alt="FinTrack Dashboard">
            </div>
            <div class="intro-text">
                <p>
                    <strong>FinTrack</strong> is an AI-powered expense tracking app that helps you effortlessly manage your financial transactions. 
                    Capture receipts through image upload, camera, or manual entry, and let our intelligent system categorize and analyze your expenses in real-time. 
                    Take control of your spending with smart, intuitive financial insights.
                </p>
                <p>
                    In today's fast-paced world, keeping track of personal finances can be overwhelming and time-consuming. 
                    FinTrack addresses this challenge by leveraging cutting-edge artificial intelligence to transform how you manage your expenses. 
                    Our innovative application goes beyond simple expense logging by providing intelligent, context-aware analysis of your financial transactions. 
                </p>
            </div>
            
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<h1 class="sub-header">Core Features</h1>',
                unsafe_allow_html=True)

    cols = st.columns(3)

    features = [
        {
            "icon": "🖼️",
            "title": "Multi-Source Receipt Input",
            "description": "Upload receipts from device, capture with camera, or enter manually. Our intelligent system processes all inputs seamlessly."
        },
        {
            "icon": "🤖",
            "title": "AI-Powered Analysis",
            "description": "Advanced machine learning algorithms extract and categorize expenses with remarkable accuracy and speed."
        },
        {
            "icon": "📊",
            "title": "Comprehensive Insights",
            "description": "Gain deep understanding of your spending patterns, track budgets, and make informed financial decisions."
        }
    ]

    for col, feature in zip(cols, features):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{feature['icon']} {feature['title']}</h3>
                <p>{feature['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<h1 class="sub-header">How FinTrack Works</h1>',
                unsafe_allow_html=True)

    work_cols = st.columns(3)
    work_steps = [
        {
            "icon": "📸",
            "title": "Capture Expense",
            "description": "Easily input receipt data through multiple channels: upload, camera, or manual entry."
        },
        {
            "icon": "🔍",
            "title": "Smart Processing",
            "description": "Our AI instantly analyzes and categorizes your expenses with cutting-edge technology."
        },
        {
            "icon": "📈",
            "title": "Financial Insights",
            "description": "Get detailed reports, spending trends, and actionable financial recommendations."
        }
    ]

    for col, step in zip(work_cols, work_steps):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{step['icon']} {step['title']}</h3>
                <p>{step['description']}</p>
            </div>
            """, unsafe_allow_html=True)

    st.markdown('<h1 class="sub-header">Advanced Technology</h1>',
                unsafe_allow_html=True)

    tech_cols = st.columns(3)
    technologies = [
        {
            "icon": "🌐",
            "title": "Web Framework",
            "description": "Streamlit - Fast, interactive web applications"
        },
        {
            "icon": "🧠",
            "title": "AI Engine",
            "description": "Google Gemini - Cutting-edge AI for intelligent processing"
        },
        {
            "icon": "📊",
            "title": "Data Management",
            "description": "Pandas & PIL - Robust data handling and image processing"
        }
    ]

    for col, tech in zip(tech_cols, technologies):
        with col:
            st.markdown(f"""
            <div class="feature-card">
                <h3>{tech['icon']} {tech['title']}</h3>
                <p class="desc">{tech['description']}</p>
            </div>
            """, unsafe_allow_html=True)


def main():
    landing_page()


if __name__ == "__main__":
    main()
