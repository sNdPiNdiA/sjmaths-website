/**
 * Simple storage implementation used only by tests.
 *
 * It behaves like browser localStorage but lives in memory.
 */

export class MemoryStorage {

    constructor() {

        this.data = {};
    }


    getItem(key) {

        if (
            Object.prototype.hasOwnProperty.call(
                this.data,
                key
            )
        ) {

            return this.data[key];
        }


        return null;
    }


    setItem(
        key,
        value
    ) {

        this.data[key] =
            String(value);
    }


    removeItem(key) {

        delete this.data[key];
    }


    clear() {

        this.data = {};
    }
}


export default MemoryStorage;
