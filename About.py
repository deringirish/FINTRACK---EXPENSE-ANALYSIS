# import streamlit as st


# def about_us_page():
#     # Custom CSS for styling
#     st.markdown("""
#     <style>
#     .about-container {
#         max-width: 800px;
#         margin: 0 auto;
#         padding: 20px;
#         background-color: #f0f4f8;
#         border-radius: 12px;
#         box-shadow: 0 6px 12px rgba(0,0,0,0.1);
#     }
#     .team-member {
#         display: flex;
#         align-items: center;
#         margin-bottom: 20px;
#         padding: 15px;
#         background-color: white;
#         border-radius: 8px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.08);
#         transition: transform 0.3s ease;
#     }
#     .team-member:hover {
#         transform: scale(1.02);
#     }
#     .team-member img {
#         width: 150px;
#         height: 150px;
#         border-radius: 50%;
#         margin-right: 20px;
#         object-fit: cover;
#         border: 4px solid #4a90e2;
#     }
#     .team-member-info h3 {
#         margin: 0 0 10px 0;
#         color: #2c3e50;
#         font-size: 1.3em;
#     }
#     .team-member-info p {
#         margin: 0;
#         color: #666;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Main content
#     st.markdown("<div class='about-container'>", unsafe_allow_html=True)

#     # Page Title
#     st.markdown("<h1 style='text-align: center; color: #2c3e50;'>About Us</h1>",
#                 unsafe_allow_html=True)

#     # College and Department Description
#     st.markdown("""
#     <p style='text-align: justify; line-height: 1.6;'>
#     We are a group of passionate students from the East Point College of Engineering and Technology, Bangalore,
#     pursuing our dreams and working together to create innovative solutions.
#     Our collaborative spirit and shared commitment to technology drive us to explore
#     and develop cutting-edge projects.
#     </p>
#     """, unsafe_allow_html=True)

#     # Team Members Section
#     st.markdown("<h2 style='color: #2c3e50;'>Our Team</h2>",
#                 unsafe_allow_html=True)

#     # Team Member 1
#     st.markdown("""
#     <div class='team-member'>
#         <img src='/api/placeholder/150/150' alt='Team Member 1'>
#         <div class='team-member-info'>
#             <h3>Derin Girish D G</h3>
#             <p>B.E - Computer Science Engineering</p>
#             <p>Passionate about software development and machine learning.
#             Skilled in Python, React, and cloud technologies.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Team Member 2
#     st.markdown("""
#     <div class='team-member'>
#         <img src='/api/placeholder/150/150' alt='Team Member 2'>
#         <div class='team-member-info'>
#             <h3>Priya Sharma</h3>
#             <p>Electronics and Communication Engineering</p>
#             <p>Enthusiastic about IoT, embedded systems,
#             and innovative electronic solutions.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Team Member 3
#     st.markdown("""
#     <div class='team-member'>
#         <img src='/api/placeholder/150/150' alt='Team Member 3'>
#         <div class='team-member-info'>
#             <h3>Aditya Patel</h3>
#             <p>Information Technology</p>
#             <p>Focused on web development, cybersecurity,
#             and creating impactful technological solutions.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Our Strengths Section
#     st.markdown("""
#     <h2 style='color: #2c3e50;'>Our Strengths</h2>
#     <ul style='line-height: 1.6;'>
#         <li>Collaborative problem-solving approach</li>
#         <li>Interdisciplinary technical skills</li>
#         <li>Passion for innovation and learning</li>
#         <li>Strong foundation in engineering principles</li>
#     </ul>
#     """, unsafe_allow_html=True)

#     # College and Project Information
#     st.markdown("""
#     <h2 style='color: #2c3e50;'>About East Point College</h2>
#     <p style='text-align: justify; line-height: 1.6;'>
#     East Point College of Engineering and Technology is a premier institution
#     dedicated to nurturing technical talent and fostering innovation.
#     Located in the heart of the city, we are committed to providing
#     world-class engineering education and preparing students for
#     the challenges of the technological landscape.
#     </p>
#     """, unsafe_allow_html=True)

#     # Contact Section
#     st.markdown("""
#     <h2 style='color: #2c3e50;'>Contact Us</h2>
#     <p>
#     Email: team@eastpoint.edu.in<br>
#     College: East Point College of Engineering and Technology<br>
#     Location: Bangalore, Karnataka
#     </p>
#     """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)


# # Run the about us page
# # about_us_page()
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#

# import streamlit as st


# def about_us_page():
#     # Custom CSS for dark theme styling
#     st.markdown("""
#     <style>
#     body {
#         background-color: #121212;
#         color: #e0e0e0;
#     }
#     .about-container {
#         max-width: 800px;
#         margin: 0 auto;
#         padding: 20px;
#         background-color: #1e1e1e;
#         border-radius: 12px;
#         box-shadow: 0 6px 12px rgba(0,0,0,0.3);
#     }
#     .team-member {
#         display: flex;
#         align-items: center;
#         margin-bottom: 20px;
#         padding: 15px;
#         background-color: #2a2a2a;
#         border-radius: 8px;
#         box-shadow: 0 4px 6px rgba(0,0,0,0.2);
#         transition: transform 0.3s ease;
#     }
#     .team-member:hover {
#         transform: scale(1.02);
#     }
#     .team-member img {
#         width: 150px;
#         height: 150px;
#         border-radius: 50%;
#         margin-right: 20px;
#         object-fit: cover;
#         border: 4px solid rgb(255, 75, 75);
#     }
#     .team-member-info h3 {
#         margin: 0 0 10px 0;
#         color: rgb(255, 75, 75);
#         font-size: 1.3em;
#     }
#     .team-member-info p {
#         margin: 0;
#         color: #a0a0a0;
#     }
#     h1, h2 {
#         color: rgb(255, 75, 75) !important;
#     }
#     </style>
#     """, unsafe_allow_html=True)

#     # Page Title
#     st.markdown("<h1 style='text-align: center;'>About Us</h1>",
#                 unsafe_allow_html=True)

#     # College and Department Description
#     st.markdown("""
#     <p style='text-align: justify; line-height: 1.6; color: #e0e0e0;'>
#     We are a group of passionate students from the East Point College of Engineering and Technology, Bangalore,
#     pursuing our dreams and working together to create innovative solutions.
#     Our collaborative spirit and shared commitment to technology drive us to explore
#     and develop cutting-edge projects.
#     </p>
#     """, unsafe_allow_html=True)

#     # Team Members Section
#     st.markdown("<h2>Our Team</h2>",
#                 unsafe_allow_html=True)

#     # Team Member 1
#     st.markdown("""
#     <div class='team-member'>
#         <div class='team-member-info'>
#             <h3>Derin Girish D G</h3>
#             <p>B.E - Computer Science Engineering</p>
#             <p>Passionate about AI, ML, and technology, I thrive on innovation and building intelligent solutions.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Team Member 2
#     st.markdown("""
#     <div class='team-member'>
#         <div class='team-member-info'>
#             <h3>Chandana B</h3>
#             <p>B.E - Computer Science Engineering</p>
#             <p>Enthusiastic in Web Development</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Team Member 3
#     st.markdown("""
#     <div class='team-member'>
#         <div class='team-member-info'>
#             <h3>Arpita V</h3>
#             <p>B.E - Computer Science Engineering</p>
#             <p>Focused on creating impactful technological solutions.</p>
#         </div>
#     </div>
#     """, unsafe_allow_html=True)

#     # Our Strengths Section
#     st.markdown("""
#     <h2>Our Strengths</h2>
#     <ul style='line-height: 1.6; color: #e0e0e0;'>
#         <li>Collaborative problem-solving approach</li>
#         <li>Interdisciplinary technical skills</li>
#         <li>Passion for innovation and learning</li>
#         <li>Strong foundation in engineering principles</li>
#     </ul>
#     """, unsafe_allow_html=True)

#     # College and Project Information
#     st.markdown("""
#     <h2>About East Point College</h2>
#     <p style='text-align: justify; line-height: 1.6; color: #e0e0e0;'>
#     East Point College of Engineering and Technology is a premier institution
#     dedicated to nurturing technical talent and fostering innovation. We are committed to providing
#     world-class engineering education and preparing students for
#     the challenges of the technological landscape.
#     </p>
#     """, unsafe_allow_html=True)

#     # Contact Section
#     st.markdown("""
#     <h2>Contact Us</h2>
#     <p style='color: #e0e0e0;'>
#     Email: <span style='color: #a0a0a0;'>team@eastpoint.edu.in</span><br>
#     College: East Point College of Engineering and Technology<br>
#     Location: Bangalore, Karnataka
#     </p>
#     """, unsafe_allow_html=True)

#     st.markdown("</div>", unsafe_allow_html=True)


# # Run the about us page
# # about_us_page()

#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
import streamlit as st


def about_us_page():
    # Custom CSS for dark theme styling
    st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: #ffffff !important;
    }
    .about-container {
        max-width: 800px;
        margin: 0 auto;
        padding: 20px;
        background-color: #1e1e1e;
        border-radius: 12px;
        box-shadow: 0 6px 12px rgba(0,0,0,0.3);
    }
    .team-member {
        display: flex;
        align-items: center;
        margin-bottom: 20px;
        padding: 15px;
        background-color: #2a2a2a;
        border-radius: 8px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }
    .team-member:hover {
        transform: scale(1.02);
    }
    .team-member img {
        width: 150px;
        height: 150px;
        border-radius: 50%;
        margin-right: 20px;
        object-fit: cover;
        border: 4px solid rgb(255, 75, 75);
    }
    .team-member-info h3 {
        margin: 0 0 10px 0;
        color: rgb(255, 75, 75);
        font-size: 1.3em;
    }
    .team-member-info p {
        margin: 0;
        color: #ffffff;
    }
    h1, h2 {
        color: rgb(255, 75, 75) !important;
    }
    </style>
    """, unsafe_allow_html=True)

    # Page Title
    st.markdown("<h1 style='text-align: center;'>About Confluence</h1>",
                unsafe_allow_html=True)

    # Team Description
    st.markdown("""
    <p style='text-align: justify; line-height: 1.6; color: #e0e0e0;'>
    Confluence is a dynamic team of innovative computer science engineers from East Point College of Engineering and Technology, Bangalore. 
    We are united by our passion for technology and our commitment to creating transformative solutions. 
    Our team thrives on collaborative problem-solving, pushing the boundaries of innovation, and developing cutting-edge technological projects.
    </p>
    """, unsafe_allow_html=True)

    # Team Members Section
    st.markdown("<h2>Our Team</h2>",
                unsafe_allow_html=True)

    # Team Member 1
    st.markdown("""
    <div class='team-member'>
        <div class='team-member-info'>
            <h3>Derin Girish D G</h3>
            <p>B.E - Computer Science Engineering</p>
            <p>Specialized in AI and Machine Learning, driving our team's technological innovation and strategic direction.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Team Member 2
    st.markdown("""
    <div class='team-member'>
        <div class='team-member-info'>
            <h3>Chandana B</h3>
            <p>B.E - Computer Science Engineering</p>
            <p>Expert in crafting responsive and innovative web solutions that bring our ideas to life.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Team Member 3
    st.markdown("""
    <div class='team-member'>
        <div class='team-member-info'>
            <h3>Arpita V</h3>
            <p>B.E - Computer Science Engineering</p>
            <p>Focused on architecting comprehensive technological solutions and ensuring project excellence.</p>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Our Strengths Section
    st.markdown("""
    <h2>Confluence: Our Strengths</h2>
    <ul style='line-height: 1.6; color: #e0e0e0;'>
        <li>Interdisciplinary approach to technological challenges</li>
        <li>Cutting-edge technical expertise across multiple domains</li>
        <li>Commitment to continuous learning and innovation</li>
        <li>Strong collaborative problem-solving capabilities</li>
    </ul>
    """, unsafe_allow_html=True)

    # College and Project Information
    st.markdown("""
    <h2>Our Academic Foundation</h2>
    <p style='text-align: justify; line-height: 1.6; color: #e0e0e0;'>
    Emerging from East Point College of Engineering and Technology, Confluence represents the pinnacle of technical education 
    and innovative potential. We are not just students, but future technology leaders committed to developing solutions 
    that can transform industries and address real-world challenges.
    </p>
    """, unsafe_allow_html=True)

    # Contact Section
    st.markdown("""
    <h2>Connect with Confluence</h2>
    <p style='color: #e0e0e0;'>
    Email: <span style='color: #a0a0a0;'>confluence.acd@gmail.com</span><br>
    Institution: East Point College of Engineering and Technology<br>
    Location: Bangalore, Karnataka
    </p>
    """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


# Run the about us page
# about_us_page()
