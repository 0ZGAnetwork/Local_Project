def add_setting(settings, pair):

    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        return f"Setting '{key}' already exists! Cannot add a new setting with this name."

    settings[key] = value

    return f"Setting '{key}' added with value '{value}' successfully!"
  
def update_setting(settings, pair):

    key, value = pair
    key = key.lower()
    value = value.lower()

    if key in settings:
        settings[key] = value
        return f"Setting '{key}' updated to '{value}' successfully!"

    return f"Setting '{key}' does not exist! Cannot update a non-existing setting."
        

def delete_setting(settings, key):

    key = key.lower()

    if key in settings:
        del settings[key]
        return f"Setting '{key}' deleted successfully!"

    return "Setting not found!"


def view_settings(settings):

    if settings == {}:
        return "No settings available."

    result = "Current User Settings:\n"

    for key, value in settings.items():
        result += f"{key.capitalize()}: {value}\n"

    return result

# --- ---
test_settings = {
    "theme": "dark",
    "notifications": "enabled",
    "volume": "high"
}

settings = {"theme": "light"}


print(view_settings(setting))
# print('\n', settings)

# print(add_setting(settings, ('THEME','dark')))
# print('\n', settings)

# print(add_setting(settings, ('volume','high')))
# print('\n', settings)

# print(update_setting(settings, ('theme', 'dark')))
# print('\n', settings)

# print(update_setting(settings, ('theme', 'light')))
# print('\n', settings)

# print(delete_setting(settings, 'theme'))
# print('\n', settings)

# print(view_settings(settings))
# print('\n', settings)

# print("\033[34mTo jest zielony tekst\033[0m")
