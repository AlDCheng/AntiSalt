# -*- mode: python -*-

block_cipher = None


a = Analysis(['Application_Main_All.py'],
             pathex=['C:\\Users\\Israel\\Desktop\\AntiSalt-master'],
             binaries=None,
             datas=None,
             hiddenimports=[],
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,
          name='Application_Main_All',
          debug=False,
          strip=False,
          upx=True,
          console=False )
