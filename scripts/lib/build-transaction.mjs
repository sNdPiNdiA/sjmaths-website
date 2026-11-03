import fs from 'node:fs';
import crypto from 'node:crypto';

// Stage beside each target so rename stays on the same volume. Failed preparation
// changes no served files; a failed commit restores previous contents. This local
// transaction is not a crash-safe deployment mechanism.
export function commitBuildWrites(writes, io = fs) {
    const prepared = [];
    const committed = [];
    const failures = [];
    const suffix = `.sj-build-${crypto.randomUUID()}`;
    try {
        for (const [target, contents] of writes) {
            const previous = io.existsSync(target) ? io.readFileSync(target) : null;
            const temporary = target + suffix;
            prepared.push({ target, temporary, previous });
            io.writeFileSync(temporary, contents, { flag: 'wx' });
        }
        for (const item of prepared) {
            let retries = 5;
            while (retries > 0) {
                try {
                    io.renameSync(item.temporary, item.target);
                    break;
                } catch (renameErr) {
                    if (renameErr.code === 'EBUSY' && --retries > 0) {
                        Atomics.wait(new Int32Array(new SharedArrayBuffer(4)), 0, 0, 80);
                    } else {
                        // A copy fallback can partially overwrite a served file
                        // before rollback knows it was changed. Fail closed.
                        throw renameErr;
                    }
                }
            }
            committed.push(item);
        }
    } catch (error) {
        failures.push(error);
        for (const item of committed.reverse()) {
            try {
                if (item.previous === null) io.unlinkSync(item.target);
                else io.writeFileSync(item.target, item.previous);
            } catch (rollbackError) { failures.push(rollbackError); }
        }
    } finally {
        for (const item of prepared) {
            try {
                if (io.existsSync(item.temporary)) io.unlinkSync(item.temporary);
            } catch (cleanupError) { failures.push(cleanupError); }
        }
    }
    if (failures.length > 1) throw new AggregateError(failures, 'Build failed and rollback or cleanup needs attention.');
    if (failures.length) throw failures[0];
}
