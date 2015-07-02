#! /usr/bin/env python
# encoding: utf-8

# these variables are mandatory ('/' are converted automatically)
top = '.'
out = 'build'

def options(ctx):
    ctx.load('compiler_c')

def configure(ctx):
    ctx.load('compiler_c')
    ctx.check_cfg(package='glib-2.0', uselib_store='GLIB', args='--cflags --libs', mandatory=True)

def setup_environment(ctx):
    WARNING_FLAGS = ['-Wall', '-Werror', '-Wno-unused-function', '-Wno-format-zero-length']
    DEBUG_FLAGS = ['-g']
    OPT_FLAGS = ['-O3']
    ctx.env.CFLAGS_default   = ['-std=gnu99', '-fPIC'] + OPT_FLAGS + WARNING_FLAGS
    ctx.env.CXXFLAGS_default = ['-std=c++11', '-fPIC'] + OPT_FLAGS + WARNING_FLAGS

def build(ctx):
    setup_environment(ctx)
    ctx.recurse('c')