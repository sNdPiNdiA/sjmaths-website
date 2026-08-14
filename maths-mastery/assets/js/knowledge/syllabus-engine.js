/**
 * SJMaths Maths Mastery
 * Syllabus Engine
 *
 * Responsibility:
 *   Provide read-only syllabus operations.
 *
 * It does not own learner progress.
 */

export class SyllabusEngine {

    constructor({
        repository
    } = {}) {

        if (!repository) {

            throw new Error(
                "SyllabusEngine: repository is required."
            );
        }


        this.repository =
            repository;
    }


    getSyllabusForExam(
        examId
    ) {

        return this.repository.loadForExam(
            examId
        );
    }


    getSyllabus(
        syllabusId
    ) {

        return this.repository.loadById(
            syllabusId
        );
    }


    getSections(
        syllabusId
    ) {

        const syllabus =
            this.getSyllabus(
                syllabusId
            );


        return Array.isArray(
            syllabus.sections
        )
            ? [
                ...syllabus.sections
            ].sort(
                (
                    a,
                    b
                ) =>
                    (
                        a.order || 0
                    ) -
                    (
                        b.order || 0
                    )
            )
            : [];
    }


    getTopicsForSection(
        syllabusId,
        sectionId
    ) {

        const section =
            this.getSections(
                syllabusId
            ).find(
                item =>
                    item.id ===
                    sectionId
            );


        if (!section) {

            return [];
        }


        return Array.isArray(
            section.topics
        )
            ? [
                ...section.topics
            ].sort(
                (
                    a,
                    b
                ) =>
                    (
                        a.order || 0
                    ) -
                    (
                        b.order || 0
                    )
            )
            : [];
    }


    getAllTopicIds(
        syllabusId
    ) {

        return this.getSections(
            syllabusId
        )
        .flatMap(
            section =>
                Array.isArray(
                    section.topics
                )
                    ? section.topics
                    : []
        )
        .sort(
            (
                a,
                b
            ) =>
                (
                    a.order || 0
                ) -
                (
                    b.order || 0
                )
        )
        .map(
            topic =>
                topic.topicId
        );
    }


    getTopicCount(
        syllabusId
    ) {

        return this.getAllTopicIds(
            syllabusId
        ).length;
    }


    getSectionCount(
        syllabusId
    ) {

        return this.getSections(
            syllabusId
        ).length;
    }


    getSummary(
        syllabusId
    ) {

        const syllabus =
            this.getSyllabus(
                syllabusId
            );


        return {

            id:
                syllabus.id,

            examId:
                syllabus.examId,

            name:
                syllabus.name,

            version:
                syllabus.version,

            sections:
                this.getSectionCount(
                    syllabusId
                ),

            topics:
                this.getTopicCount(
                    syllabusId
                )

        };
    }

}
