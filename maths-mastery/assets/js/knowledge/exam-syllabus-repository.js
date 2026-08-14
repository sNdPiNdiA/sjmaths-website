/**
 * SJMaths Maths Mastery
 *
 * Versioned Exam Syllabus Repository
 *
 * Responsibility:
 *   Load versioned, exam-specific syllabus records.
 *
 * Does NOT:
 *   - decide whether an exam officially contains a topic
 *   - modify learner progress
 *   - calculate mastery
 *   - select questions
 */

import fs from "fs";
import path from "path";


export class ExamSyllabusRepository {

    constructor({
        rootDir
    } = {}) {

        this.rootDir =
            rootDir ||
            path.resolve(
                process.cwd(),
                "maths-mastery",
                "data",
                "exams"
            );
    }


    listExamDirectories() {

        if (
            !fs.existsSync(
                this.rootDir
            )
        ) {

            return [];
        }


        return fs.readdirSync(
            this.rootDir,
            {
                withFileTypes: true
            }
        )

        .filter(
            entry =>
                entry.isDirectory()
        )

        .map(
            entry =>
                entry.name
        )

        .filter(
            name =>
                !name.startsWith("_")
        )

        .sort();
    }


    listSyllabusVersions(
        examId
    ) {

        const examDir =
            this.getExamDirectory(
                examId
            );


        if (
            !fs.existsSync(
                examDir
            )
        ) {

            return [];
        }


        return fs.readdirSync(
            examDir,
            {
                withFileTypes: true
            }
        )

        .filter(
            entry =>
                entry.isDirectory()
        )

        .map(
            entry =>
                entry.name
        )

        .sort();
    }


    load(
        examId,
        version
    ) {

        if (!examId) {

            throw new Error(
                "ExamSyllabusRepository: examId is required."
            );
        }


        if (!version) {

            throw new Error(
                "ExamSyllabusRepository: syllabus version is required."
            );
        }


        const filePath =
            path.join(
                this.getExamDirectory(
                    examId
                ),
                version,
                "syllabus.json"
            );


        return this.loadFile(
            filePath
        );
    }


    loadLatest(
        examId
    ) {

        const versions =
            this.listSyllabusVersions(
                examId
            );


        if (
            versions.length === 0
        ) {

            return null;
        }


        return this.load(
            examId,
            versions[
                versions.length - 1
            ]
        );
    }


    getExamDirectory(
        examId
    ) {

        return path.join(
            this.rootDir,
            examId
        );
    }


    loadFile(
        filePath
    ) {

        if (
            !fs.existsSync(
                filePath
            )
        ) {

            throw new Error(
                `ExamSyllabusRepository: file not found: ${filePath}`
            );
        }


        const raw =
            fs.readFileSync(
                filePath,
                "utf8"
            );


        const clean =
            raw.charCodeAt(0) ===
                0xFEFF
                ? raw.slice(1)
                : raw;


        return JSON.parse(
            clean
        );
    }

}
