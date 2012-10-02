#!/usr/bin/env python
import pace

from chat import CHAT
from pace_entity import *

TEST_CVC = "\x7F\x21\x82\x01\x41\x7F\x4E\x81\xFA\x5F\x29\x01\x00\x42\x0D\x5A\x5A\x44\x56\x43\x41\x41\x54\x41\x30\x30\x30\x33\x7F\x49\x4F\x06\x0A\x04\x00\x7F\x00\x07\x02\x02\x02\x02\x03\x86\x41\x04\x19\xD1\x75\x45\xD3\xFE\x0B\x34\x3E\x7E\xE2\xAE\x4E\x2B\xC9\x2D\x51\x35\x1C\xC1\x17\xA4\x7F\xA9\x51\x9A\xDB\x1E\x40\x5E\xE6\xB8\x12\x12\x80\xBC\xC2\xFF\xF0\x35\x7A\x19\x7D\xE7\x39\xA7\xFD\x2E\xF0\x22\x10\xEF\x34\x3C\xDB\xE7\x9E\xF9\x4B\x8E\x28\x59\x1B\xB9\x5F\x20\x0B\x5A\x5A\x44\x4B\x42\x32\x30\x30\x30\x30\x52\x7F\x4C\x12\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x02\x02\x53\x05\x00\x03\x01\xDF\x04\x5F\x25\x06\x01\x00\x00\x02\x01\x07\x5F\x24\x06\x01\x00\x00\x03\x03\x01\x65\x5E\x73\x2D\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x03\x01\x80\x20\x75\xE0\xC4\xAC\x36\xC2\x5A\x33\xAC\x0E\x9A\x75\xEB\x79\x2A\x72\xF3\x31\xA5\x1E\x28\x63\x4E\xCC\x2E\xD6\x2E\x54\xF3\xC6\x93\xDA\x73\x2D\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x03\x02\x80\x20\x18\x12\x65\x74\x49\xFC\xF1\xD3\xDA\xD8\x3D\x13\x14\x29\x17\x5C\x61\x8B\x21\xBA\xF0\xAF\x44\xAC\xE3\x8C\xB2\xC1\x2C\xEB\x2A\x56\x5F\x37\x40\x54\x0F\x85\x09\x12\xAB\xD3\x51\xF8\xF5\x56\x9B\x53\x4A\x5C\x8F\x64\x54\x5B\x51\xA7\x34\x70\xBE\x5A\xD2\x89\xC1\x9A\x5E\x13\x52\x53\xD3\xBB\x15\x52\x26\x21\x7B\x41\xE7\xF0\x68\xB3\x52\x3F\x3A\x63\x92\x22\xAF\x2B\x62\x8C\x39\x7D\x4F\xD4\x02\x1E\xDE\x00\xDC"


TEST_DESCRIPTION = "\x30\x82\x01\x90\x06\x0A\x04\x00\x7F\x00\x07\x03\x01\x03\x01\x01\xA1\x16\x0C\x14\x42\x75\x6E\x64\x65\x73\x64\x72\x75\x63\x6B\x65\x72\x65\x69\x20\x47\x6D\x62\x48\xA2\x24\x13\x22\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x62\x75\x6E\x64\x65\x73\x64\x72\x75\x63\x6B\x65\x72\x65\x69\x2E\x64\x65\x2F\x64\x76\x63\x61\xA3\x18\x0C\x16\x44\x65\x75\x74\x73\x63\x68\x65\x20\x4B\x72\x65\x64\x69\x74\x62\x61\x6E\x6B\x20\x41\x47\xA4\x13\x13\x11\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x6B\x62\x2E\x64\x65\xA5\x82\x01\x13\x0C\x82\x01\x0F\x54\x61\x75\x62\x65\x6E\x73\x74\x72\x2E\x20\x37\x2D\x39\x0D\x0A\x31\x30\x31\x31\x37\x20\x42\x65\x72\x6C\x69\x6E\x0D\x0A\x69\x6E\x66\x6F\x40\x64\x6B\x62\x2E\x64\x65\x0D\x0A\x45\x72\xC3\xB6\x66\x66\x6E\x75\x6E\x67\x20\x65\x69\x6E\x65\x73\x20\x4B\x6F\x6E\x74\x6F\x73\x0D\x0A\x42\x65\x72\x6C\x69\x6E\x65\x72\x20\x42\x65\x61\x75\x66\x74\x72\x61\x67\x74\x65\x72\x20\x66\xC3\xBC\x72\x20\x44\x61\x74\x65\x6E\x73\x63\x68\x75\x74\x7A\x20\x75\x6E\x64\x20\x49\x6E\x66\x6F\x72\x6D\x61\x74\x69\x6F\x6E\x73\x66\x72\x65\x69\x68\x65\x69\x74\x2C\x20\x41\x6E\x20\x64\x65\x72\x20\x55\x72\x61\x6E\x69\x61\x20\x34\x2D\x31\x30\x2C\x20\x31\x30\x37\x38\x37\x20\x42\x65\x72\x6C\x69\x6E\x2C\x20\x30\x33\x30\x2F\x31\x33\x20\x38\x38\x39\x2D\x30\x2C\x20\x6D\x61\x69\x6C\x62\x6F\x78\x40\x64\x61\x74\x65\x6E\x73\x63\x68\x75\x74\x7A\x2D\x62\x65\x72\x6C\x69\x6E\x2E\x64\x65\x2C\x20\x68\x74\x74\x70\x3A\x2F\x2F\x77\x77\x77\x2E\x64\x61\x74\x65\x6E\x73\x63\x68\x75\x74\x7A\x2D\x62\x65\x72\x6C\x69\x6E\x2E\x64\x65\x0D\x0A\x45\x72\xC3\xB6\x66\x66\x6E\x75\x6E\x67\x20\x65\x69\x6E\x65\x73\x20\x4B\x6F\x6E\x74\x6F\x73\x0D\x0A"

CVCA = "\x7f\x21\x82\x02\xf3\x7f\x4e\x82\x02\x6a\x5f\x29\x01\x00\x42\x0d\x44\x45\x43\x56\x43\x41\x41\x54\x30\x30\x30\x30\x31\x7f\x49\x82\x02\x1f\x06\x0a\x04\x00\x7f\x00\x07\x02\x02\x02\x02\x05\x81\x40\xaa\xdd\x9d\xb8\xdb\xe9\xc4\x8b\x3f\xd4\xe6\xae\x33\xc9\xfc\x07\xcb\x30\x8d\xb3\xb3\xc9\xd2\x0e\xd6\x63\x9c\xca\x70\x33\x08\x71\x7d\x4d\x9b\x00\x9b\xc6\x68\x42\xae\xcd\xa1\x2a\xe6\xa3\x80\xe6\x28\x81\xff\x2f\x2d\x82\xc6\x85\x28\xaa\x60\x56\x58\x3a\x48\xf3\x82\x40\x78\x30\xa3\x31\x8b\x60\x3b\x89\xe2\x32\x71\x45\xac\x23\x4c\xc5\x94\xcb\xdd\x8d\x3d\xf9\x16\x10\xa8\x34\x41\xca\xea\x98\x63\xbc\x2d\xed\x5d\x5a\xa8\x25\x3a\xa1\x0a\x2e\xf1\xc9\x8b\x9a\xc8\xb5\x7f\x11\x17\xa7\x2b\xf2\xc7\xb9\xe7\xc1\xac\x4d\x77\xfc\x94\xca\x83\x40\x3d\xf9\x16\x10\xa8\x34\x41\xca\xea\x98\x63\xbc\x2d\xed\x5d\x5a\xa8\x25\x3a\xa1\x0a\x2e\xf1\xc9\x8b\x9a\xc8\xb5\x7f\x11\x17\xa7\x2b\xf2\xc7\xb9\xe7\xc1\xac\x4d\x77\xfc\x94\xca\xdc\x08\x3e\x67\x98\x40\x50\xb7\x5e\xba\xe5\xdd\x28\x09\xbd\x63\x80\x16\xf7\x23\x84\x81\x81\x04\x81\xae\xe4\xbd\xd8\x2e\xd9\x64\x5a\x21\x32\x2e\x9c\x4c\x6a\x93\x85\xed\x9f\x70\xb5\xd9\x16\xc1\xb4\x3b\x62\xee\xf4\xd0\x09\x8e\xff\x3b\x1f\x78\xe2\xd0\xd4\x8d\x50\xd1\x68\x7b\x93\xb9\x7d\x5f\x7c\x6d\x50\x47\x40\x6a\x5e\x68\x8b\x35\x22\x09\xbc\xb9\xf8\x22\x7d\xde\x38\x5d\x56\x63\x32\xec\xc0\xea\xbf\xa9\xcf\x78\x22\xfd\xf2\x09\xf7\x00\x24\xa5\x7b\x1a\xa0\x00\xc5\x5b\x88\x1f\x81\x11\xb2\xdc\xde\x49\x4a\x5f\x48\x5e\x5b\xca\x4b\xd8\x8a\x27\x63\xae\xd1\xca\x2b\x2f\xa8\xf0\x54\x06\x78\xcd\x1e\x0f\x3a\xd8\x08\x92\x85\x40\xaa\xdd\x9d\xb8\xdb\xe9\xc4\x8b\x3f\xd4\xe6\xae\x33\xc9\xfc\x07\xcb\x30\x8d\xb3\xb3\xc9\xd2\x0e\xd6\x63\x9c\xca\x70\x33\x08\x70\x55\x3e\x5c\x41\x4c\xa9\x26\x19\x41\x86\x61\x19\x7f\xac\x10\x47\x1d\xb1\xd3\x81\x08\x5d\xda\xdd\xb5\x87\x96\x82\x9c\xa9\x00\x69\x86\x81\x81\x04\x64\xf0\x9c\x61\x7c\x0d\x5a\x4e\x2e\x88\xb2\x59\x8a\xf0\x68\x60\x44\x0c\x07\xc5\xed\x35\x3a\x18\xa1\x4e\x93\x8a\x6c\xbc\xe3\x05\x94\xd9\x40\x79\x59\x4c\xcf\xae\xfe\x28\xd9\xaa\xc9\xac\x1b\xd3\x7c\x89\xb6\xcc\xbd\x10\xb1\x4f\xc3\xaa\x19\xde\xb1\xfd\x03\xea\x15\x1a\x42\xb8\x92\x54\x7a\x33\x96\x18\xc4\xc9\xf2\x6f\xa9\x83\x85\x5d\x89\x3f\x81\x41\x3c\xd3\x20\xea\x42\x30\xd3\x41\x5e\xbc\xcd\xb5\x90\x8d\x91\xdc\x23\xc6\x56\x6f\x47\xb8\xa0\xe0\xa1\x9c\x17\x5b\xdc\x77\x5d\x88\x24\x67\x6a\xac\xfa\xed\xea\x0c\x16\x0e\x87\x01\x01\x5f\x20\x0d\x44\x45\x43\x56\x43\x41\x41\x54\x30\x30\x30\x30\x31\x7f\x4c\x0e\x06\x09\x04\x00\x7f\x00\x07\x03\x01\x02\x01\x53\x01\xc3\x5f\x25\x06\x01\x00\x00\x09\x03\x00\x5f\x24\x06\x01\x01\x00\x09\x02\x05\x5f\x37\x81\x80\xa5\xe7\x22\x44\xd0\xac\x9c\xd3\xe8\xfe\x9b\x87\x8e\xa3\x2a\x24\xf4\xaa\x06\x0f\xd1\x7c\x2a\x82\x91\xd9\x79\x7e\x8a\x60\xf2\x8a\x29\x78\xe3\xf4\xea\xe8\x40\xe9\x5b\x6a\x64\xfd\xa4\x4d\x8d\x39\xa6\x99\x52\x1c\xd5\x38\x22\x03\x96\x49\x45\x15\x0a\x6c\xc4\xa5\x0c\x49\xee\x23\x4a\xb3\x6d\xf6\x75\xe4\x4c\x11\x49\x90\x80\x67\x6d\xd5\xb3\xac\x18\x59\xd9\x8b\x30\x2c\xa9\x60\x5c\xd9\x4a\x51\xd7\xda\x57\x38\xbe\xaa\x49\x84\x8b\xca\x77\x77\xb7\xdc\x9a\xcc\xda\xa1\xd0\xb6\x44\x32\xb2\xc1\x38\x89\xa4\x85\x4c\x9f\xf3\x46"

EF_CARDSECURITY = "\x30\x82\x07\xE7\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x07\x02\xA0\x82\x07\xD8\x30\x82\x07\xD4\x02\x01\x03\x31\x0F\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\x30\x82\x01\x4D\x06\x08\x04\x00\x7F\x00\x07\x03\x02\x01\xA0\x82\x01\x3F\x04\x82\x01\x3B\x31\x82\x01\x37\x30\x0D\x06\x08\x04\x00\x7F\x00\x07\x02\x02\x02\x02\x01\x02\x30\x12\x06\x0A\x04\x00\x7F\x00\x07\x02\x02\x03\x02\x02\x02\x01\x02\x02\x01\x01\x30\x12\x06\x0A\x04\x00\x7F\x00\x07\x02\x02\x04\x02\x02\x02\x01\x02\x02\x01\x0D\x30\x1C\x06\x09\x04\x00\x7F\x00\x07\x02\x02\x03\x02\x30\x0C\x06\x07\x04\x00\x7F\x00\x07\x01\x02\x02\x01\x0D\x02\x01\x01\x30\x2F\x06\x08\x04\x00\x7F\x00\x07\x02\x02\x06\x16\x23\x68\x74\x74\x70\x73\x3A\x2F\x2F\x77\x77\x77\x2E\x68\x6A\x70\x2D\x63\x6F\x6E\x73\x75\x6C\x74\x69\x6E\x67\x2E\x63\x6F\x6D\x2F\x68\x6F\x6D\x65\x30\x17\x06\x0A\x04\x00\x7F\x00\x07\x02\x02\x05\x02\x03\x30\x09\x02\x01\x01\x02\x01\x01\x01\x01\x00\x30\x17\x06\x0A\x04\x00\x7F\x00\x07\x02\x02\x05\x02\x03\x30\x09\x02\x01\x01\x02\x01\x02\x01\x01\xFF\x30\x19\x06\x09\x04\x00\x7F\x00\x07\x02\x02\x05\x02\x30\x0C\x06\x07\x04\x00\x7F\x00\x07\x01\x02\x02\x01\x0D\x30\x62\x06\x09\x04\x00\x7F\x00\x07\x02\x02\x01\x02\x30\x52\x30\x0C\x06\x07\x04\x00\x7F\x00\x07\x01\x02\x02\x01\x0D\x03\x42\x00\x04\xA4\x4E\xBE\x54\x51\xDF\x7A\xAD\xB0\x1E\x45\x9B\x8C\x92\x8A\x87\x74\x6A\x57\x92\x7C\x8C\x28\xA6\x77\x5C\x97\xA7\xE1\xFE\x8D\x9A\x46\xFF\x4A\x1C\xC7\xE4\xD1\x38\x9A\xEA\x19\x75\x8E\x4F\x75\xC2\x8C\x59\x8F\xD7\x34\xAE\xBE\xB1\x35\x33\x7C\xF9\x5B\xE1\x2E\x94\x02\x01\x01\xA0\x82\x04\x62\x30\x82\x04\x5E\x30\x82\x02\x92\xA0\x03\x02\x01\x02\x02\x03\x01\x63\x26\x30\x41\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x0A\x30\x34\xA0\x0F\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA1\x1C\x30\x1A\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x08\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA2\x03\x02\x01\x20\x30\x53\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x44\x45\x31\x17\x30\x15\x06\x03\x55\x04\x0A\x0C\x0E\x48\x4A\x50\x20\x43\x6F\x6E\x73\x75\x6C\x74\x69\x6E\x67\x31\x17\x30\x15\x06\x03\x55\x04\x0B\x0C\x0E\x43\x6F\x75\x6E\x74\x72\x79\x20\x53\x69\x67\x6E\x65\x72\x31\x12\x30\x10\x06\x03\x55\x04\x03\x0C\x09\x48\x4A\x50\x20\x50\x42\x20\x43\x53\x30\x1E\x17\x0D\x30\x39\x30\x39\x31\x38\x30\x37\x35\x39\x35\x33\x5A\x17\x0D\x31\x30\x30\x39\x31\x33\x30\x37\x35\x39\x35\x33\x5A\x30\x54\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x44\x45\x31\x17\x30\x15\x06\x03\x55\x04\x0A\x0C\x0E\x48\x4A\x50\x20\x43\x6F\x6E\x73\x75\x6C\x74\x69\x6E\x67\x31\x18\x30\x16\x06\x03\x55\x04\x0B\x0C\x0F\x44\x6F\x63\x75\x6D\x65\x6E\x74\x20\x53\x69\x67\x6E\x65\x72\x31\x12\x30\x10\x06\x03\x55\x04\x03\x0C\x09\x48\x4A\x50\x20\x50\x42\x20\x44\x53\x30\x82\x01\x22\x30\x0D\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x01\x05\x00\x03\x82\x01\x0F\x00\x30\x82\x01\x0A\x02\x82\x01\x01\x00\xB6\xC5\xA8\xEE\x57\x30\x76\x79\xE3\x64\xE3\xF7\xE7\x76\xEA\x64\x07\x4E\x9A\x72\xF6\xB3\x76\xC2\xD2\x31\x89\x63\x1C\x10\xBA\x65\xEA\x34\x6F\xEF\x70\x3B\x52\xEF\x75\x93\xD4\x96\xE1\x50\x0F\x71\x64\xD0\x38\xE9\xA8\x80\xD0\x6E\x90\xFC\xF9\x6F\xAD\x5B\x60\x68\xB3\x42\xCC\xA8\x24\x77\x0B\xAD\xF1\x42\x9E\xBB\xDB\x97\x88\x0A\xAE\xA4\x31\x14\x62\xCA\xCE\x40\xAA\xF2\x24\x78\x35\xAB\xC2\x59\x1E\x18\x80\xAD\xD9\xFD\x35\xF2\xC0\xE4\x3C\xC6\xFE\xB9\x1B\x0F\x13\x7C\xC4\x2A\xD8\x34\x73\x24\x93\xFD\x63\xF7\x8F\xC7\xDA\x75\xCD\xB4\xA1\xBD\x4C\x7D\xE1\xE0\x4A\xC1\xB4\xBD\x4C\x62\xC4\x6F\x8D\x83\xEE\x6B\xF1\xAC\x24\x05\xD5\xA1\x73\x77\x6A\x58\x96\x0A\x79\xB1\xB5\xB9\x0B\x79\x7A\x4A\x7A\x19\x84\x57\xC7\xA0\x2A\x72\xA2\xFF\x9A\x32\x7E\x55\x88\x19\x67\x42\xC5\x7C\x8B\x9D\x5E\xE6\x4B\x8A\x46\x00\x3B\xC5\x6D\x24\x93\xC0\xA6\x58\x82\x37\x94\xAB\x23\x14\xBC\xF9\x79\xC5\xEE\xDF\x32\x7C\x6C\x11\x2E\x9E\xDD\x86\xC6\xE4\x19\xF9\xAD\x35\xA9\x46\x56\xFD\xE7\xED\x89\x6A\xF5\xC3\x46\x43\x5A\xB3\xD7\xBE\xC0\xF8\xB9\x02\x56\xA3\x10\x50\xB3\x97\x02\x03\x01\x00\x01\xA3\x52\x30\x50\x30\x1F\x06\x03\x55\x1D\x23\x04\x18\x30\x16\x80\x14\x0D\xFD\x5C\x02\x88\xBF\xEC\xE0\xB0\x7A\x5D\x40\xFF\x80\xAC\x8A\x91\x74\x3A\x9B\x30\x1D\x06\x03\x55\x1D\x0E\x04\x16\x04\x14\x91\x93\xF4\xF0\xAA\x4A\xCA\xC0\xD3\xA1\xB6\xAC\x83\xB2\x4F\x6F\xDC\x8F\xF2\x1B\x30\x0E\x06\x03\x55\x1D\x0F\x01\x01\xFF\x04\x04\x03\x02\x07\x80\x30\x41\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x0A\x30\x34\xA0\x0F\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA1\x1C\x30\x1A\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x08\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA2\x03\x02\x01\x20\x03\x82\x01\x81\x00\xA3\xAF\xEC\x3B\xC5\xD3\x66\xE6\x61\x19\x4A\xCA\x8D\xFC\x39\x06\x76\x06\x1D\x6E\x52\x30\x18\xCA\x13\x93\x0D\x79\x40\xE6\xCE\x77\x86\x1D\x18\xF6\x5F\x3C\xEF\x8C\xBF\x44\xE8\x7D\x59\xAA\xFA\x6F\x29\xEC\x57\xFB\x19\xDB\x12\x30\xF0\xF2\xFC\x1B\xF6\x0D\x1D\x03\x96\x33\x3C\x89\xA9\x2B\xF2\x31\x3C\x43\x60\xBA\xB2\x18\xDE\x57\x71\x3F\x39\x0C\xA5\xBB\xB6\x99\xCD\x1A\x1E\x27\x3C\x61\x8B\x25\xA7\xEE\xDA\xB5\xF0\xBA\xB0\x30\x65\xAA\x74\x9D\x51\x32\x60\xBE\x86\x7E\xB0\x11\x29\x1D\xCF\x4A\xDC\x83\x33\xF7\x78\x4F\xDD\xE8\x17\x2F\x46\xC4\xF7\x90\x42\x15\xFD\xC9\x8F\x5C\xDE\x49\x16\xF0\x3E\x24\x9C\xD3\x94\x07\x62\xD2\xF8\xE9\x2F\x23\x17\x16\xA6\xBF\x74\x2F\xED\xC2\x62\x7E\x62\xF0\x46\x95\x6D\xB9\x7B\xAA\xD2\x5C\x04\x62\x47\x54\xD4\xAF\x3E\x1A\x7E\xC4\x72\x07\xCC\x08\xBD\x15\x4E\x83\x9A\x43\x55\xD0\x1F\x16\xDA\x2C\xC1\x61\x77\xA9\x14\xD4\x42\x87\xE6\x52\x25\x64\xD0\x00\x53\x9E\xC9\x6A\x2B\x0E\x1E\x6E\xBB\x89\x63\x81\x86\x8B\x5A\xFE\x0A\x0F\xD3\xC3\x62\xF4\x19\xAF\xFD\xFF\x01\x6A\x71\x17\x0A\xC8\xB3\x78\xA6\xE3\x99\x5D\x82\xEE\x45\x95\x0E\xEB\xB4\xC9\xBB\xF6\x31\x13\x24\x82\xA5\x03\xC3\x10\x26\xB4\xC2\xCD\x94\x26\xE6\x66\x3D\xE4\xC4\x3E\xFE\x54\x01\xF4\xD3\xBA\x76\xE5\x4F\x66\x3B\x28\x32\x3E\xA3\x33\x1E\x96\xA7\x08\x12\xF9\x43\x15\xD6\x08\xA9\xE8\xCE\x1B\xF0\x2B\x6E\xCF\x07\x01\x5D\x40\xF4\x73\xDF\xE1\x6F\x5C\x12\x14\x60\x81\xC4\x4C\x14\x8D\xAB\x09\x83\x50\x46\x57\xA5\x3C\xCA\x16\xBD\x54\x5D\x5A\xD5\x9A\x21\xAA\x91\x9E\x7F\x9B\xB7\xB3\x50\x01\xAB\xEF\x61\xE7\xD5\x6E\x21\xC7\xF1\x13\x73\x42\x55\x71\xA7\x91\x45\xD4\x46\x2E\xB2\x6B\x31\x82\x02\x05\x30\x82\x02\x01\x02\x01\x01\x30\x5A\x30\x53\x31\x0B\x30\x09\x06\x03\x55\x04\x06\x13\x02\x44\x45\x31\x17\x30\x15\x06\x03\x55\x04\x0A\x0C\x0E\x48\x4A\x50\x20\x43\x6F\x6E\x73\x75\x6C\x74\x69\x6E\x67\x31\x17\x30\x15\x06\x03\x55\x04\x0B\x0C\x0E\x43\x6F\x75\x6E\x74\x72\x79\x20\x53\x69\x67\x6E\x65\x72\x31\x12\x30\x10\x06\x03\x55\x04\x03\x0C\x09\x48\x4A\x50\x20\x50\x42\x20\x43\x53\x02\x03\x01\x63\x26\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA0\x4A\x30\x17\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x09\x03\x31\x0A\x06\x08\x04\x00\x7F\x00\x07\x03\x02\x01\x30\x2F\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x09\x04\x31\x22\x04\x20\x49\xAE\xB9\x37\x52\x8C\x26\x9E\xA7\x23\xBB\xC8\xAA\xDC\x38\x5C\x9D\x6B\x1A\xE3\x75\x16\xA5\xB8\x92\x1F\xF8\xC4\x59\x18\x72\x93\x30\x41\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x0A\x30\x34\xA0\x0F\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA1\x1C\x30\x1A\x06\x09\x2A\x86\x48\x86\xF7\x0D\x01\x01\x08\x30\x0D\x06\x09\x60\x86\x48\x01\x65\x03\x04\x02\x01\x05\x00\xA2\x03\x02\x01\x20\x04\x82\x01\x00\x97\xC2\x2D\x87\xC3\x13\xD6\x48\xDF\xB9\xDE\x9D\x9C\xCA\x3A\x41\xCB\xF8\x52\x22\xE3\x6D\x3B\x9C\x7E\xB1\xCC\x0B\x1A\x8C\xAE\x4C\x93\xE0\xF1\xCA\x02\x8A\x90\xDD\x2B\x4F\x5C\xB4\x2C\x9E\x5B\xB5\x73\xC0\x39\x77\x3E\x64\x08\x41\xB3\x28\x30\xDF\x83\x93\x22\x46\xFC\x8B\xAF\x92\x8D\x67\x54\x6E\x8E\x0C\x06\x65\xA9\x32\x87\x48\x85\x51\x8E\xA3\xD0\x20\x46\xA6\x18\xCF\x1A\xF5\xA0\xF5\xE4\xC4\x05\x62\x4D\x2D\x66\xD1\x6B\xDA\x18\xA8\x38\x22\x84\x78\x8E\x81\xFE\x1C\xB5\xE2\x17\x01\xCD\xD2\x09\x22\x12\x0E\x68\x20\x30\xE8\x0D\x12\xDA\x40\x6B\x01\x36\xE9\xED\x8B\x23\x8F\x65\x3C\x7D\xDC\xA9\x27\x86\x60\x41\x4E\xFA\x93\x73\x82\x50\xCD\x08\x41\x72\x7E\x0F\x68\xC4\x90\x02\x64\x1D\x7E\x40\x26\x28\x5B\x9B\x53\xF2\x70\xBB\xA5\x05\x8E\x46\x60\x0B\x84\x35\x54\x60\x5B\xF8\xEC\x2C\x74\x0A\xED\xC8\xB2\x4E\x2A\x64\xAC\x78\xF5\x89\x97\xA1\x88\x33\xA4\x05\xCB\x64\xEA\x6D\xD7\xD7\x11\x5F\xD7\xC3\x51\x76\x72\x65\x4E\x03\x02\x97\x30\xFA\xB7\x25\x65\xA0\x92\x65\x71\x01\xF3\xFE\x5A\x63\xCF\x70\x92\x0A\x11\x2F\xCF\x69\x29\x37\xA3"

def pacetest():
    picc = PICC("123456")
    pcd = PCD("123456")

    enc_nonce = picc.generate_nonce()
    pcd.decrypt_nonce(enc_nonce)
    picc_pub = picc.get_static_pubkey()
    pcd_pub = pcd.get_static_pubkey()
    picc.perform_mapping(pcd_pub)
    pcd.perform_mapping(picc_pub)
    picc_eph_pub = picc.generate_ephemeral_pubkey()
    pcd_eph_pub = pcd.generate_ephemeral_pubkey()
    picc.compute_shared_secret(pcd_eph_pub)
    pcd.compute_shared_secret(picc_eph_pub)
    picc.derive_keys()
    pcd.derive_keys()
    token_pcd = pcd.get_authentication_token()

    print(picc)
    print(pcd)

    picc.EAC_CTX_set_encryption_ctx()
    ENCRYPTION_TEST = "TESTTESTTESTTEST"
    encrypted = picc.encrypt(ENCRYPTION_TEST)

    decrypted = pcd.decrypt(encrypted)
    if (decrypted != ENCRYPTION_TEST):
        raise PACEException("Failed to decrypt test data")

    mac = picc.authenticate(ENCRYPTION_TEST)
    if (not mac):
        raise PACEException("Failed to authenticate testdata")

    id_picc = picc.EAC_Comp()

    if (picc.verify_authentication_token(token_pcd) == 1):
        print("PACE run was successful")
    else:
        print("An error occured")

def cvctest():
    cvc = pace.CVC_d2i_CVC_CERT(TEST_CVC)
    cvc_desc = pace.d2i_CVC_CERTIFICATE_DESCRIPTION(TEST_DESCRIPTION)
    chat = pace.cvc_get_chat(cvc)
    pace.cvc_chat_print(chat, 4)

    asn1_chat="\x7F\x4C\x12\x06\x09\x04\x00\x7F\x00\x07\x03\x01\x02\x02\x53\x05\x00\x01\x01\x98\x04"

    chat = CHAT(asn1_chat)
    print(chat)
    print(chat.get_role())
    print(chat.get_terminal_type())
    print(chat.get_relative_authorizations())
    pace.CVC_CERT_free(cvc)
    pace.CVC_CERTIFICATE_DESCRIPTION_free(cvc_desc)

def tatest():
    ta = PACEEntity("123456")

    if pace.EAC_CTX_init_ca(ta.ctx, pace.id_CA_ECDH_AES_CBC_CMAC_128, 11, None, None) == 0:
        raise PACEException("Failed to initialize context", "Chip Authentication", "PICC")

    if pace.EAC_CTX_init_ta(ta.ctx, None, CVCA, None) == 0:
        raise PACEException("Failed to initialize context", "Terminal Authentication", "PICC")

    pace.TA_STEP2_import_certificate(ta.ctx, TEST_CVC)

    nonce = pace.TA_STEP4_get_nonce(ta.ctx)
    if nonce is None:
        raise PACEException("Failed to generate nonce", "Terminal Authentication", "PICC")

def catest():
    pace.CA_get_pubkey(EF_CARDSECURITY)

def oidtest():
    print(pace.OBJ_txt2nid("id-CA-ECDH-AES-CBC-CMAC-128"))
    print(pace.id_CA_ECDH_AES_CBC_CMAC_128)
    assert(pace.OBJ_txt2nid("id-CA-ECDH-AES-CBC-CMAC-128") == pace.id_CA_ECDH_AES_CBC_CMAC_128)

if __name__ == "__main__":
    pacetest()
    cvctest()
    tatest()
    catest()
    oidtest()
