config.load_autoconfig()

c.tabs.background = True
c.new_instance_open_target = 'window'
c.downloads.position = 'bottom'
c.spellcheck.languages = ['en-US']


c.url.searchengines = {"DEFAULT": "https://www.google.com/search?q={}"}
config.bind('<Shift-Left>', 'back')
config.bind('<Shift-Down>', 'tab-next')
config.bind('<Shift-Up>', 'tab-prev')
config.bind('<Shift-Right>', 'forward')
c.content.javascript.enabled = True
c.editor.command: ["kitty", "-e", "nvim", "{}"]
config.source('gruvbox.py')
