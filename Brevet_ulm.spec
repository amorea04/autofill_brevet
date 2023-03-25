# -*- mode: python ; coding: utf-8 -*-


block_cipher = None

added_files = [
         ( 'docs', 'docs' ),
         ('logo0.ico', '.'), 
         ('logo0.jpg', '.'), 
         ('/Users/Adrien/Documents/paramoteur/autofill_brevet/autofill_brevet/lib/python3.9/site-packages/customtkinter', 'customtkinter'),
         ]

exclude_libs = [
    'black', 'IPython', 'fitz', 'jedi', 'lib2to3', 
    'markupsafe', 'parso', 'psutil', 'tornado', 'zmq'
]

a = Analysis(
    ['gui_autofill.py'],
    pathex=[],
    binaries=[],
    datas=added_files,
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=exclude_libs,
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)
pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='Brevet_ulm',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='Brevet_ulm',
)
app = BUNDLE(
    coll,
    name='Brevet_ulm.app',
    icon='logo0.ico',
    bundle_identifier=None,
)
