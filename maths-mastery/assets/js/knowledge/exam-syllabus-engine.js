/**
 * SJMaths Maths Mastery
 *
 * Versioned Exam Syllabus Engine
 *
 * Read-only domain operations over syllabus records.
 */

export class ExamSyllabusEngine {

    constructor({
        repository
    } = {}) {

        if (!repository) {

            throw new Error(
                "ExamSyllabusEngine: repository is required."
            );
        }


        this.repository =
            repository;
    }


    getSyllabus(
        examId,
        version
    ) {

        return this.repository.load(
            examId,
            version
        );
    }


    getLatestSyllabus(
        examId
    ) {

        return this.repository.loadLatest(
            examId
        );
    }


    getSections(
        examId,
        version
    ) {

        const syllabus =
            this.getSyllabus(
                examId,
                version
            );


        return Array.isArray(
            syllabus?.syllabus?.sections
        )
            ? syllabus.syllabus.sections
            : [];
    }


    getIncludedTopics(
        examId,
        version
    ) {

        const sections =
            this.getSections(
                examId,
                version
            );


        const topics = [];


        for (
            const section
            of sections
        ) {

            for (
                const topic
                of Array.isArray(
                    section.topics
                )
                    ? section.topics
                    : []
            ) {

                if (
                    topic.included === true
                ) {

                    topics.push(
                        topic
                    );
                }
            }
        }


        return topics;
    }


    getIncludedSubtopics(
        examId,
        version
    ) {

        const topics =
            this.getIncludedTopics(
                examId,
                version
            );


        const subtopics = [];


        for (
            const topic
            of topics
        ) {

            for (
                const subtopic
                of Array.isArray(
                    topic.subtopics
                )
                    ? topic.subtopics
                    : []
            ) {

                if (
                    subtopic.included === true
                ) {

                    subtopics.push(
                        subtopic
                    );
                }
            }
        }


        return subtopics;
    }


    getVerificationStatus(
        examId,
        version
    ) {

        const syllabus =
            this.getSyllabus(
                examId,
                version
            );


        return (
            syllabus?.syllabus?.verification?.status ||
            "unverified"
        );
    }


    getSummary(
        examId,
        version
    ) {

        const syllabus =
            this.getSyllabus(
                examId,
                version
            );


        return {

            examId,

            version,

            status:
                syllabus?.syllabus?.status ||
                "draft",

            verificationStatus:
                this.getVerificationStatus(
                    examId,
                    version
                ),

            sections:
                this.getSections(
                    examId,
                    version
                ).length,

            topics:
                this.getIncludedTopics(
                    examId,
                    version
                ).length,

            subtopics:
                this.getIncludedSubtopics(
                    examId,
                    version
                ).length

        };
    }

}
