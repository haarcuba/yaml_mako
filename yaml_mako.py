import yaml
import mako.template

def load( yamlSource, ** kwargs ):
    content = yamlSource.read()
    template = mako.template.Template( content )
    yamlContent = template.render( ** kwargs )
    return yaml.load( yamlContent )

def load_all( yamlSource, ** kwargs ):
    content = yamlSource.read()
    template = mako.template.Template( content )
    yamlContent = template.render( ** kwargs )
    return yaml.load_all( yamlContent )
