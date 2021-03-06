from OpenGL.GL import *

ProgramFiles = ['simple.glsl']

Programs = {
    "BareBones" : {
        "GL_VERTEX_SHADER" : "simple.xforms simple.vert",
        "GL_GEOMETRY_SHADER" : "simple.xforms simple.geom",
        "GL_FRAGMENT_SHADER" : "simple.xforms simple.frag"
    }
}

class Attribs:
    POSITION = 0
    NORMAL = 1

def load_shaders(glslFiles = ProgramFiles, attribs = Attribs, programMap = Programs):
    """Parse a series of simple text files, each of which is composed
    series of shader snippets. The given 'attribs' class defines an
    enumeration of attribute slots to bind (aka semantics).
        
    In each text files, lines starting with two dash characters start a new
    shader snippet with the given name.  For example:
       -- S1
       uniform float foo;
       -- Prefix
       #version 150
       -- S2
       uniform float bar;
    """

    # First parse the file to populate 'snippetMap'
    class ParserState:
        HEADER = 0
        SOURCE = 1
    parserState = ParserState.HEADER
    snippetMap = {}
    for glslFile in glslFiles:
        snippetPrefix = glslFile.split('.')[0] + '.'
        for line in open(glslFile):
            if line.startswith('--'):
                if parserState is ParserState.HEADER:
                    parserState = ParserState.SOURCE
                elif len(source):
                    snippetMap[snippetName] = ''.join(source)
                snippetName = snippetPrefix + line[2:].strip()
                source = []
                continue
            if parserState is ParserState.HEADER:
                pass
            else:
                source.append(line)
    if len(source):
        snippetMap[snippetName] = ''.join(source)

    # Now, glue together the strings and feed them to OpenGL
    stagePrefix = "#version 150\n"
    programs = {}
    for key, val in programMap.items():
        programHandle = glCreateProgram()
        for stageName, snippetList in val.items():
            snippets = map(snippetMap.get, snippetList.split())
            stageSource = stagePrefix + ''.join(snippets)
            stage = getattr(OpenGL.GL, stageName)
            sHandle = glCreateShader(stage)
            glShaderSource(sHandle, stageSource)
            glCompileShader(sHandle)
            success = glGetShaderiv(sHandle, GL_COMPILE_STATUS)
            if not success:
                print 'Error in', stageName, snippetList
                infolog = glGetShaderInfoLog(sHandle)
                raise SystemExit(infolog)
            glAttachShader(programHandle, sHandle)
        for attrib in dir(attribs):
            if attrib.startswith('__'):
                continue
            slot = getattr(attribs, attrib)
            name = attrib[0] + attrib[1:].lower()
            glBindAttribLocation(programHandle, slot, name)
        glLinkProgram(programHandle)
        success = glGetProgramiv(programHandle, GL_LINK_STATUS);
        if not success:
            infolog = glGetProgramInfoLog(programHandle)
            raise SystemExit(infolog)
        programs[key] = programHandle
    return programs
