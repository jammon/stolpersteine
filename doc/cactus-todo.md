# Cactus-Todo

## Plugins
- Most plugins should be part of cactus and not part the users project.
- They should be developped and maintained with cactus and not with some other (example-) project like CactusBlog.
- They should be enabled and disabled in a config file and not by renaming the source code.
- The sequence of execution should be configurable.
- It should be defined in the configs, not in the code, which files each plugin works on (usually depending on the file extension).
- Plugins for markup languages like markdown or haml should handle the extension in a configurable manner, e.g.
    + change it to `.html`,
    + leave it as it is,
    + save the output file without extension.

## Work path
- The input files should be read once, processed in memory and then the output files should be written to disk.

(I'm open for discussion on this last point. It seems natural to me, but there may be solid arguments to handle it differently.)
