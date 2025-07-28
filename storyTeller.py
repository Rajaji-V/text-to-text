def generate_story_text():
  
    name = input("Enter the character's name: ")
    activity = input("Enter their favorite activity: ")
    setting = input("Enter the story place: ")

    if not name or not activity or not setting:
        print("Please fill all fields.")
        return

    prompt = f"Once upon a time in {setting}, there was a young person named {name}. They loved {activity} more than anything in the world."

    print("\nGenerating story, please wait...")

   
    story = story_generator(prompt, max_length=150, num_return_sequences=1)[0]['generated_text']

    
    print("\n--- Your Personalized Story ---\n")
    print(story)

generate_story_text()