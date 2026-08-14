/**
 * SJMaths Maths Mastery
 *
 * Progress Repository Contract
 *
 * The application talks to this contract.
 * It does NOT talk directly to localStorage.
 */

export class ProgressRepository {

    async load() {

        throw new Error(
            "ProgressRepository.load() must be implemented."
        );
    }


    async save(progress) {

        throw new Error(
            "ProgressRepository.save() must be implemented."
        );
    }


    async clear() {

        throw new Error(
            "ProgressRepository.clear() must be implemented."
        );
    }
}


export default ProgressRepository;
