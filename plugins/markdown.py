# -*- coding: utf-8 -*-
import os
import markdown
import codecs
import logging

from cactus.utils.filesystem import fileList


template = """
%s

{%% extends "%s" %%}
{%% block %s %%}

%s

{%% endblock %%}
"""

CLEANUP = []


def isMarkdown(path):
    return path.endswith('.md')


def getMeta(md, item, default):
    try:
        return md.Meta[item][0]
    except Exception:
        return default


def preBuild(site):
    for path in fileList(site.paths['pages']):
        if not isMarkdown(path):
            continue
        md = markdown.Markdown(extensions=['markdown.extensions.meta'])
        logging.debug('Path: %s', path)
        print 'Path: %s!' % path

        # read and convert markdown file
        with codecs.open(path, 'r', encoding='utf-8') as f:
            html = md.convert(f.read())

        # get metadata
        metadata = []
        for k, v in md.Meta.iteritems():
            metadata.append('%s: %s' % (k, v[0]))
            for extra_v in v[1:]:
                metadata.append('    %s' % (extra_v,))

        # write html-file
        outPath = path.replace('.md', '.html')
        with codecs.open(outPath, 'w', encoding='utf-8') as f:
            data = template % (
                '\n'.join(metadata),
                getMeta(md, 'extends', 'base.html'),
                getMeta(md, 'block', 'body-container'),
                html
            )
            f.write(data)

        CLEANUP.append(outPath)


def postBuild(site):
    global CLEANUP
    for path in CLEANUP:
        os.remove(path)
    CLEANUP = []
