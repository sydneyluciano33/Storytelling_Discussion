import streamlit as st

import altair as alt
import pandas as pd
source = [{
    "Bacteria": "Aerobacter aerogenes",
    "Penicillin": 870,
    "Streptomycin": 1,
    "Neomycin": 1.6,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Bacillus anthracis",
    "Penicillin": 0.001,
    "Streptomycin": 0.01,
    "Neomycin": 0.007,
    "Gram_Staining": "positive",
    "Genus": "other"
  },
  {
    "Bacteria": "Brucella abortus",
    "Penicillin": 1,
    "Streptomycin": 2,
    "Neomycin": 0.02,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Diplococcus pneumoniae",
    "Penicillin": 0.005,
    "Streptomycin": 11,
    "Neomycin": 10,
    "Gram_Staining": "positive",
    "Genus": "other"
  },
  {
    "Bacteria": "Escherichia coli",
    "Penicillin": 100,
    "Streptomycin": 0.4,
    "Neomycin": 0.1,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Klebsiella pneumoniae",
    "Penicillin": 850,
    "Streptomycin": 1.2,
    "Neomycin": 1,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Mycobacterium tuberculosis",
    "Penicillin": 800,
    "Streptomycin": 5,
    "Neomycin": 2,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Proteus vulgaris",
    "Penicillin": 3,
    "Streptomycin": 0.1,
    "Neomycin": 0.1,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Pseudomonas aeruginosa",
    "Penicillin": 850,
    "Streptomycin": 2,
    "Neomycin": 0.4,
    "Gram_Staining": "negative",
    "Genus": "other"
  },
  {
    "Bacteria": "Salmonella (Eberthella) typhosa",
    "Penicillin": 1,
    "Streptomycin": 0.4,
    "Neomycin": 0.008,
    "Gram_Staining": "negative",
    "Genus": "Salmonella"
  },
  {
    "Bacteria": "Salmonella schottmuelleri",
    "Penicillin": 10,
    "Streptomycin": 0.8,
    "Neomycin": 0.09,
    "Gram_Staining": "negative",
    "Genus": "Salmonella"
  },
  {
    "Bacteria": "Staphylococcus albus",
    "Penicillin": 0.007,
    "Streptomycin": 0.1,
    "Neomycin": 0.001,
    "Gram_Staining": "positive",
    "Genus": "Staphylococcus"
  },
  {
    "Bacteria": "Staphylococcus aureus",
    "Penicillin": 0.03,
    "Streptomycin": 0.03,
    "Neomycin": 0.001,
    "Gram_Staining": "positive",
    "Genus": "Staphylococcus"
  },
  {
    "Bacteria": "Streptococcus fecalis",
    "Penicillin": 1,
    "Streptomycin": 1,
    "Neomycin": 0.1,
    "Gram_Staining": "positive",
    "Genus": "Streptococcus"
  },
  {
    "Bacteria": "Streptococcus hemolyticus",
    "Penicillin": 0.001,
    "Streptomycin": 14,
    "Neomycin": 10,
    "Gram_Staining": "positive",
    "Genus": "Streptococcus"
  },
  {
    "Bacteria": "Streptococcus viridans",
    "Penicillin": 0.005,
    "Streptomycin": 10,
    "Neomycin": 40,
    "Gram_Staining": "positive",
    "Genus": "Streptococcus"
  }]

st.title("Positive Gram Staining Bacteria is No Match for Penicillin")
options = {
    "Mechanism of Action": "Penicillin works by inhibiting the synthesis of bacterial cell walls, which is particularly effective against Gram-positive bacteria.",
    "History": "Penicillin was discovered by Alexander Fleming in 1928 and has since saved countless lives by treating bacterial infections.",
    "Usage": "Penicillin is commonly used to treat infections caused by Gram-positive bacteria, such as strep throat and pneumonia.",
    "Effectiveness": "Penicillin is highly effective against positive Gram staining bacteria.",
    "Resistance": "Some bacteria have developed resistance to penicillin, making it less effective against certain strains.",
    "Side Effects": "While generally safe, penicillin can cause allergic reactions in some individuals, ranging from mild rashes to severe anaphylaxis.",
}
choice = st.selectbox("Learn more about Penicillin Here:", list(options.keys()))
st.write(options[choice])
st.markdown("<br><br>", unsafe_allow_html=True)

options2 = {
    "What is Gram Staining?": "Gram staining is a laboratory technique used to differentiate bacterial species into two groups based on the characteristics of their cell walls: Gram-positive and Gram-negative.",
    "Importance of Gram Staining": "Gram staining is crucial in microbiology as it helps identify the type of bacteria, guiding appropriate treatment options.",
    "Gram-Positive Bacteria": "These bacteria have a thick peptidoglycan layer in their cell walls, which retains the crystal violet stain used in the Gram staining process, appearing purple under a microscope.",
    "Gram-Negative Bacteria": "These bacteria have a thinner peptidoglycan layer and an outer membrane, which does not retain the crystal violet stain, appearing pink after the counterstain is applied.",
}
choice2 = st.selectbox("Learn more about Gram Staining Here:", list(options2.keys()))
st.write(options2[choice2])
st.write(" ")
st.markdown("<br><br>", unsafe_allow_html=True)

source_df = pd.DataFrame(source)
highlight = alt.selection_point(on='mouseover', fields=['Bacteria'], nearest=True)
chart = alt.Chart(source_df).mark_circle().encode(
    x='Bacteria',
    y='Penicillin',
    color='Gram_Staining',
    tooltip=['Bacteria', 'Penicillin', 'Gram_Staining'],
    size=alt.condition(highlight, alt.value(200), alt.value(100))
    ).properties(
        title = "Penicillin is Highly Effective vs. Positive Gram Staining Bacteria ",
        width = 600,
        height = 400
    ).add_params(
        highlight
    )
annotation = alt.Chart(source_df).mark_text(
    align='center',
    baseline='middle',
    dx=0,
    dy = -19,
    fontSize=15
).transform_filter(
    # Filter condition: only show text for points where Penicillin > 100
    alt.datum.Penicillin == 0.005
).encode(
    x='Bacteria',
    y='Penicillin',
    text='Penicillin',
)
second_annotation = alt.Chart(source_df).mark_text(
        align='center',
        baseline='middle',
        dx=0,
        dy=-29,
        fontSize=15 # Use a different dy to avoid overlap with the first annotation
    ).transform_filter(
        (alt.datum.Penicillin > 0.007) & (alt.datum.Penicillin < 1)
    ).encode(
        x='Bacteria',
        y='Penicillin',
        text='Penicillin',
)
third_annotation = alt.Chart(source_df).mark_text(
        align='center',
        baseline='middle',
        dx=0,
        dy=-9,
        fontSize=15 # Use a different dy to avoid overlap with the first annotation
    ).transform_filter(
        (alt.datum.Penicillin < 0.005)
    ).encode(
        alt.X('Bacteria', axis=alt.Axis(title='Bacteria')),
        alt.Y('Penicillin', axis = alt.Axis(title='Penicillin')),
        text='Penicillin',
)
fourth_annotation = alt.Chart(source_df).mark_text(
        align='center',
        baseline='middle',
        dx=0,
        dy=-19,
        fontSize=15 # Use a different dy to avoid overlap with the first annotation
    ).transform_filter(
        (alt.datum.Penicillin > 0.005) & (alt.datum.Penicillin < 0.03)
    ).encode(
        x='Bacteria',
        y='Penicillin',
        text='Penicillin',
)
fifth_annotation = alt.Chart(source_df).mark_text(
        align='center',
        baseline='middle',
        dx=0,
        dy=-39,
        fontSize=15# Use a different dy to avoid overlap with the first annotation
    ).transform_filter(
        (alt.datum.Penicillin == 1) & (alt.datum.Gram_Staining == 'positive')
    ).encode(
        x='Bacteria',
        y='Penicillin',
        text='Penicillin',
)
rectangle_data = pd.DataFrame({
    'x_start': ['Bacillus anthracis'],
    'x_end': ['Streptococcus viridans'],
    'y_start': [0],
    'y_end': [100]
})

# Create the rectangle mark
rect = alt.Chart(rectangle_data).mark_rect().encode(
    x='x_start:N',  # Encode the starting Bacteria on the x-axis (Nominal type)
    x2='x_end:N',    # Encode the ending Bacteria on the x-axis (Nominal type)
    y='y_start:Q',  # Encode the starting Penicillin on the y-axis (Quantitative type)
    y2='y_end:Q',    # Encode the ending Penicillin on the y-axis (Quantitative type)
    opacity=alt.value(0.2), # Make the rectangle semi-transparent
    color=alt.value('gray') # Set the color of the rectangle
)

chart + annotation + second_annotation + third_annotation + fourth_annotation + fifth_annotation + rect


st.markdown(
    "<span style='font-size:22px'><b>The chart above shows the effectiveness of Penicillin against various bacteria, highlighting the gram staining classification. Bacteria with positive gram staining are particularly susceptible to Penicillin, as indicated by the annotations and the rectangle highlighting the range of effectiveness in which Penicillin is able to stop all positive gram staining bacteria.</b></span>",
    unsafe_allow_html=True
)

st.markdown("<br><br>", unsafe_allow_html=True)

boxplot = alt.Chart(source_df).mark_boxplot(size=80).encode(
   x=alt.X('Gram_Staining:N', title='Gram Staining'),
    y=alt.Y('Penicillin:Q', title='Penicillin (units)',scale=alt.Scale(type='log')),
    color='Gram_Staining:N'
).properties(
    title='Penicillin Effectiveness by Gram Staining (Log Scale)',
)

st.altair_chart(boxplot, use_container_width=True)

st.markdown(
    "<span style='font-size:22px'><b>The boxplot further emphasizes how the range in which the Penicillin dosage needed for positive gram staining bacteria is much smaller than for negative gram staining bacteria. Hover over the plots on the graph to get further information.</b></span>",
    unsafe_allow_html=True
)
