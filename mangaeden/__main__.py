#!/usr/bin/env python3
# -*- coding: utf-8

import sys
import args


p = args.init_parser()
args.set_arguments(p)
p.parse_args()
