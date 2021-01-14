# gimp-keyboard-color

## About

This GIMP plugin allows you to quickly select a particular foreground color using one-letter color abbreviations on your keyboard. The key mappings and colors can be easily customized.

I recommend mapping the plugin to a keyboard shortcut, such as `Alt + O`.

## Future

It would be better if the plugin used a custom Python dialog. Currently, there is no way to display feedback in the input dialog before the user submits it, which is when GIMP runs the plugin. There is also a slight delay between running the keyboard shortcut and the input dialog being initialized.

It also seems impossible to have Vim-like keybindings where you don't need to press Enter after typing the abbreviation.

## Existing Default Keyboard Shortcuts

By default, `9` and `0` are mapped to choosing the previous and next color in a palette. These will compare against the current foreground color (for example if you selected it with this plugin), even if it the foreground color does not appear selected in the Palette Editor. Since this works instantly, it might be a better workflow.

You can select colors from an image with the Color Picker Tool (activated with `O` or by holding `Ctrl` when using a paint tool).

For arbitrary colors, you could bind a keyboard shortcut to the built-in foreground color selection dialog.
