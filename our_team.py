import streamlit as st
from PIL import Image

# Modified colored_header function
def custom_colored_header(label, description=None, color_name="blue"):
    st.markdown(
        f"""
        <div style="padding:5px;">
            <h2 style="color: {color_name}; font-size: 30px; margin-bottom: 0;">{label}</h2>
            <hr style="border: 2px solid {color_name}; margin-top: 5px; margin-bottom: 10px;">
            {'<p style="color: black; font-size: 20px; margin-top: 5px;">' + description + '</p>' if description else ''}
        </div>
        """,
        unsafe_allow_html=True
    )

def show_our_team():
    # Page Title and Subtitle
    st.title(':blue[ABOUT OUR DATASET]')
    left_column, mid_column, right_column = st.columns(3)
    
    # Team Members Section
    with left_column:
        custom_colored_header(label="Dr Do Duc Tan", color_name="blue")
        st.markdown("""
        <div style="font-size: 25px;">
        <strong>The "firestarter" manager</strong>: Beside an excellent science lecturer in VGU, Dr Tan also has another side job as the team's manager. No one can doubt his logic and innovation in "instructing our team" on this football project! To him, there is "no comfort zone": as long as we need, he is there to help and inspire us to think out of the box and make the best of everything.
        </div>
        """, unsafe_allow_html=True)

    with mid_column:
        custom_colored_header(label="Nguyen Ngoc Minh Chau", color_name="blue")
        st.markdown("""
        <div style="font-size: 25px;">
        <strong>The "spiderman" goalkeeper and "exemplary" captain:</strong> She normally looks "clowny", but, with nerves of steel and a thick face, she is a master of protecting our "net of honor"! If the team does something foolish (mostly she does herself), she will take full responsibility for those harsh criticisms and discriminations for the whole team.
        </div>
        """, unsafe_allow_html=True)

    with right_column:
        custom_colored_header(label="Pham Hong Van Anh", color_name="blue")
        st.markdown("""
        <div style="font-size: 25px;">
        <strong>The "rock-solid" defender:</strong> Maybe she is not a star in tennis, but that is a different story in football! Without knowledge in football, she plays wildly and grabs anything that comes her way on the field. With that passion and insanity, she is "like a huge rock" preventing anyone from approaching the goal where her brother goalkeeper stands.
        </div>
        """, unsafe_allow_html=True)

    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        custom_colored_header(label="Tran Tu Anh", color_name="blue")
        st.markdown("""
        <div style="font-size: 25px;">
        <strong>The "playmaker" midfielder "without a lung":</strong> Despite looking easygoing with her smiles, she should never be underestimated in the "field of creativity". A master of Photoshop and Canva, she "designs every output" offensive plan for the team. Also known for her dynamic energy, she can handle "every deadline in every hotspot", even in the latest seconds!
        </div>
        """, unsafe_allow_html=True)

    with mid_column:
        custom_colored_header(label="Pham Bao Khoi", color_name="blue")
        st.markdown("""
        <div style="font-size: 25px;">
        <strong>The "headquarter" midfielder:</strong> Within the squad, he possesses the most solid knowledge base of "pre-coding" tactics for the play. Every move in the play will go through his feet, so his brain has drawn the roadmap before the play even occurs! He shouts out both hurtful insults and constructive feedback to his teammates right on the field "for motivation."
        </div>
        """, unsafe_allow_html=True)

    with right_column:
        custom_colored_header(label="Le Bao Chau", color_name="blue")
        st.markdown("""
        <div style="font-size: 25px;">
        <strong>The "sharp-cut" attacker:</strong> As a master of languages, she uses her acute and damaging arguments like a sharp knife to cut through every defensive line of the opponents. Never after her words can people resist her attacks and shots and counterattack! That is why our striker is inevitably always the undisputable top goal scorer of the league.
        </div>
        """, unsafe_allow_html=True)

    # Team Introduction Section
    left_column, right_column = st.columns([0.6, 0.4], gap="small")
    with left_column:
        custom_colored_header(label="Team Tam Quoc", description="Coached by Dr Do Duc Tan", color_name="blue")
        image_path = 'TAm quoc.jpg'  # Adjust the path according to your environment
        image = Image.open(image_path)
        original_width = image.size[0]
        new_width = int(original_width * 0.3)
        st.image(image, width=new_width, use_column_width=True)

    with right_column:
        custom_colored_header(label="From VGU", description="Vietnamese-German University", color_name="blue")
        image_path2 = 'VGU python.png'
        image2 = Image.open(image_path2)
        st.image(image2, use_column_width=True)

if __name__ == "__main__":
    show_our_team()
