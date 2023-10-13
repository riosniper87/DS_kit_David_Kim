#!/usr/bin/env python
# coding: utf-8

# In[2]:


import streamlit as st
import random


# In[4]:


def generate_random_kkodle_word():
    with open("kkodle_words.txt", "r") as f:
        words = f.readlines()
        random_word = random.choice(words).strip()
        return random_word


# In[5]:


def check_guess(guess, word):
    colors = []
    for i in range(5):
        if guess[i] == word[i]:
            colors.append("green")
        elif guess[i] in word:
            colors.append("yellow")
        else:
            colors.append("gray")
    return colors


# In[6]:


def display_game_state(word, guess, colors):
    st.write(f"Word: {word}")
    st.write(f"Guess: {guess}")
    st.write(f"Colors: {colors}")


# In[11]:


def main():
    # Generate a random Kkodle word
#     word = generate_random_kkodle_word()
    word = "ㅂㅜㄴㅅㅣㄹ"
    # Initialize the game state
    guess = ""
    colors = []

    # Display the game state
    display_game_state(word, guess, colors)

    # Start the game loop
    while len(colors) < 6:
        # Get the user's guess
#         guess = st.text_input("Guess a word:")
        guess = "ㄱㅜㄴㅈㅣㅂ"
        # Check the guess
        colors = check_guess(guess, word)

        # Display the game state
        display_game_state(word, guess, colors)

        # If the guess is correct, end the game
        if guess == word:
            break

    # If the user runs out of guesses, they lose
    if len(colors) == 6:
        st.write("You lose!")
    else:
        st.write("You win!")

if __name__ == "__main__":
    main()

