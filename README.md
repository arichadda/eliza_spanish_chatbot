# ELIZA Spanish Chatbot

### To Test 
Run the `spanish_eliza_test.py` file using `python3 spanish_eliza_test.py`. 
To run call the `eliza()` funciton in `spanish_eliza_bot.py`

### History 

It was initially devised as a simple humanistic psychotherapeutic interaction. By using regex to parse inputs, it could prompt the user to delve deeper into the statement made in their previous sentence. While ELIZA likely would not have surpassed the Turing test, it does demonstrate how powerful simply parsing inputs and generating outputs with that information can be when it comes to conversation. The ELIZA system was initally defined in this [paper](https://dl.acm.org/doi/10.1145/365153.365168). Credit to Prof. Coto-Solano for this exercise. 

### Examples 
I1: Me llamo Ari.
O1: Hola, Ari. ¿Cómo estás?

I2: Estoy un poco triste.
O2: ¿Porqué estás triste?

I3: Porque mi mamá quiere que yo me vaya de la casa.
O3: Cuéntame más de tu mamá.

I4: Ella dice que debo ordenar el cuarto. 
O4: ¿Porqué debes ordenar el cuarto?

I5: Es que yo soy bastante desordenado. 
O5: Porqué eres desordenado?

I6: ¡Porque me da la gana!
O6: Cuéntame más.

I7: No, estúpida.
O7: ¡Hey, sin insultos! Cálmate y cuéntame más.

I8: Bueno. No sé. Me cuesta mucho. No puedo ser ordenado.
O8: ¿Porque no puedes ser ordenado?

I9: Porque cuando era niño siempre me gustaba jugar en la naturaleza, donde todo es libre.
O9: ¿Puedes darme un ejemplo específico?

I10: Pienso que todo empezó cuando fui a la playa por primera vez.
O10: ¿Porqué piensas eso?
