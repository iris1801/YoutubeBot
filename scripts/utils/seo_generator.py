import random

def generate_seo_title_and_description():
    titles = [
        "10 Mind-Blowing Facts About Space! 🚀✨",
        "10 Incredible Facts About The Ocean! 🌊🐙",
        "10 Strange Facts About Animals! 🦊🦉",
        "10 Fascinating Facts About The Human Body! 🧠💪",
    ]
    descriptions = [
        "Discover amazing facts that will blow your mind! Subscribe for more mind-blowing discoveries!",
        "Learn more about our incredible world! Hit like and comment your favorite fact!",
        "Dive into the mysteries of the universe with us! Subscribe and don't miss out!",
    ]
    return random.choice(titles), random.choice(descriptions)