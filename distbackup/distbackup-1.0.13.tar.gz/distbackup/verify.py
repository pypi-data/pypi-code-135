import logging

from .database import BackupDB
from .sourcefile import SourceFile
from .utils import hash_relpath

log = logging.getLogger(__name__)

class Verifier:
    def __init__(self, db:BackupDB):
        self.db:BackupDB = db

    def verify(self, error_fp=None, minhash=''):
        self.db.require_disk()
        self.db.current_disk.migrate_data()
        vlog = logging.getLogger(f'verify-{self.db.current_disk.name}')

        bad_objects = []
        try:
            for hash, fpath, stat in self.db.current_disk.walk_data():
                if hash <= minhash:
                    continue
                row = self.db.query_one('SELECT last_modified, size, virtual_path, ino FROM file_tree WHERE hash = ? LIMIT 1', (hash,))
                if not row:
                    vlog.warning(f'{hash} deleted or not in database')
                    continue

                lastmod, size, path, ino = row
                try:
                    srcf = SourceFile(fpath, fpath.lstat())
                except OSError as e:
                    vlog.warning(f'cannot read {fpath} ({e})')
                    continue

                if srcf.size != size:
                    msg = f'{path}: size mismatch ({srcf.size} != {size})'
                    vlog.error(msg)
                    bad_objects.append((path, hash))
                    if error_fp:
                        error_fp.write(f'{self.db.current_disk.name}\t{hash_relpath(hash)}\t{size}\t{path}\tsize={srcf.size}\n')
                        error_fp.flush()
                    continue

                vlog.info(f'check {path} ({hash})')
                srcf.copy()
                if srcf.hash != hash:
                    msg = f'{path}: hash ({srcf.hash} != {hash})'
                    vlog.error(msg)
                    bad_objects.append((path, hash))
                    if error_fp:
                        error_fp.write(f'{self.db.current_disk.name}\t{hash_relpath(hash)}\t{size}\t{path}\thash={srcf.hash}\n')
                        error_fp.flush()
        except KeyboardInterrupt:
            pass

        if bad_objects:
            vlog.info('')
            vlog.info('Bad files:')
            for path, hash in bad_objects:
                vlog.info(f'  {hash} {path}')
        else:
            vlog.info('No bad files.')
