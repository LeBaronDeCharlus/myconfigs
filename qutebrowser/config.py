config.load_autoconfig()

c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'
c.spellcheck.languages = ['en-US']

config.unbind("<ctrl+tab>")
config.bind("<ctrl+tab>", "tab-next")
config.bind("<ctrl+shift+tab>", "tab-prev")

c.input.insert_mode.auto_load = True
c.auto_save.session = True
c.downloads.location.directory = "$HOME/Downloads/"

c.url.default_page = "https://google.com"

c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}"}
config.bind('<Shift-Left>', 'back')
config.bind('<Shift-Down>', 'tab-next')
config.bind('<Shift-Up>', 'tab-prev')
config.bind('<Shift-Right>', 'forward')
c.content.javascript.enabled = True
c.editor.command: ["kitty", "-e", "nvim", "{}"]
config.source('gruvbox.py')
