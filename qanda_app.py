import streamlit as st

from transformers import AutoTokenizer, AutoModel, RetriBertTokenizer, AutoModelForSeq2SeqLM

model_name = "vblagoje/bart_eli5"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSeq2SeqLM.from_pretrained(model_name)

documents = ["when the skin is completely wet. The body continuously loses water by evaporation but the most significant amount of heat loss occurs during periods of increased physical activity. Evaporative cooling Evaporative cooling happens when water vapor is added to the surrounding air. The energy needed to evaporate the water is taken from the air in the form of sensible heat and converted into latent heat, while the air remains at a constant enthalpy. Latent heat describes the amount of heat that is needed to evaporate the liquid; this heat comes from the liquid itself and the surrounding gas and surfaces.",
                "at greater pressures. There is an ambiguity, however, as to the meaning of the terms 'heating' and 'cooling' in Sandstrom's theorem. So far, heating and cooling has always been interpreted in the literature as being associated with 'surface heating' and 'surface cooling' respectively. In real fluids, however, molecular and turbulent diffusion always cause internal heating/cooling even in absence of external heating/cooling, as long as the temperature of the fluid considered is non-uniform. As is well-known, molecular and turbulent diffusion tends to relax the system toward thermodynamic equilibrium, i.e., toward an isothermal state, which for a statically stable fluid, will warm up",
                "are not in a relation of thermal equilibrium, heat will flow from the hotter to the colder, by whatever pathway, conductive or radiative, is available, and this flow will continue until thermal equilibrium is reached and then they will have the same temperature. One form of thermal equilibrium is radiative exchange equilibrium. Two bodies, each with its own uniform temperature, in solely radiative connection, no matter how far apart, or what partially obstructive, reflective, or refractive, obstacles lie in their path of radiative exchange, not moving relative to one another, will exchange thermal radiation, in net the hotter transferring energy to",
                "air condition and moving along a line of constant enthalpy toward a state of higher humidity. A simple example of natural evaporative cooling is perspiration, or sweat, secreted by the body, evaporation of which cools the body. The amount of heat transfer depends on the evaporation rate, however for each kilogram of water vaporized 2,257 kJ of energy (about 890 BTU per pound of pure water, at 95 °F (35 °C)) are transferred. The evaporation rate depends on the temperature and humidity of the air, which is why sweat accumulates more on humid days, as it does not evaporate fast enough. Vapor-compression refrigeration uses evaporative cooling,",            
                "Thermal contact conductance In physics, thermal contact conductance is the study of heat conduction between solid bodies in thermal contact. The thermal contact conductance coefficient, , is a property indicating the thermal conductivity, or ability to conduct heat, between two bodies in contact. The inverse of this property is termed thermal contact resistance. Factors influencing contact conductance Thermal contact conductance is a complicated phenomenon, influenced by many factors. Experience shows that the most important ones are as follows: Contact pressure For thermal transport between two contacting bodies, such as particles in a granular medium, the contact pressure is the factor"]

def main():
    st.set_page_config(
        page_title="Qanda app",
        layout="wide",
        initial_sidebar_state="expanded"
    )

    st.title('Ask an interesting question')

    question = st.text_input('Enter a question')

    voice = st.checkbox('Enable voice')

    confirm_button = st.button('Get an answer')

    st.markdown(
        "<hr />",
        unsafe_allow_html=True
    )

    if confirm_button:
        with st.spinner("Generating recipe..."):

            query = question

            conditioned_doc = "<P> " + " <P> ".join([d for d in documents])

            query_and_docs = "question: {} context: {}".format(query, conditioned_doc)

            model_input = tokenizer([(query_and_docs, "A")], truncation=True, padding=True, return_tensors="pt")

            generated_answers_encoded = model.generate(input_ids=model_input["input_ids"],
                                                    attention_mask=model_input["attention_mask"],
                                                    min_length=30,
                                                    max_length=100,
                                                    do_sample=False, 
                                                    early_stopping=True,
                                                    num_beams=8,
                                                    temperature=1.0,
                                                    top_k=None,
                                                    top_p=None,
                                                    eos_token_id=tokenizer.eos_token_id,
                                                    no_repeat_ngram_size=3,
                                                    num_return_sequences=1,
                                                    decoder_start_token_id=tokenizer.bos_token_id)

            generated_answers = tokenizer.batch_decode(generated_answers_encoded, skip_special_tokens=True,clean_up_tokenization_spaces=True)


            if generated_answers:
                generated_answer = generated_answers

                st.markdown(
                    " ".join([
                        "<div>",
                        "<h2 class='font-title text-bold'>The answer:</h2>",
                        '<div style="padding: 30px;background-color: #B6C9B1; border-radius: 10px;">',
                        f'<p>{generated_answer}</p>',
                        "</div>",
                        "</div>"
                    ]),
                    unsafe_allow_html=True
                )

                if voice:
                    st.markdown(
                        " ".join([
                            "<div style='padding: 20px;background-color: #A7BFC7; border-radius: 10px;margin-top: 30px;'>",
                            '<p>Audio Coming soon...</p>',
                            "</div>"
                        ]),
                        unsafe_allow_html=True
                    )

main()