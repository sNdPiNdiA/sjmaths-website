/**
 * SJMaths Maths Mastery
 * Syllabus Repository
 *
 * Responsibility:
 *   Load syllabus definitions.
 *
 * Does NOT:
 *   calculate mastery
 *   select questions
 *   mutate learner progress
 *   implement exam logic
 */

import fs from "fs";
import path from "path";


export class SyllabusRepository {

    constructor({
        rootDir
    } = {}) {

        this.rootDir =
            rootDir ||
            path.resolve(
                process.cwd(),
                "maths-mastery",
                "data",
                "syllabi"
            );
    }


    listSyllabusFiles() {

        if (
            !fs.existsSync(
                this.rootDir
            )
        ) {

            return [];
        }


        return fs.readdirSync(
            this.rootDir
        )
        .filter(
            file =>
                file.endsWith(
                    ".json"
                )
        )
        .sort();
    }


    loadById(
        syllabusId
    ) {

        if (!syllabusId) {

            throw new Error(
                "SyllabusRepository: syllabusId is required."
            );
        }


        const filePath =
            path.join(
                this.rootDir,
                `${syllabusId}.json`
            );


        return this.loadFile(
            filePath
        );
    }


    loadForExam(
        examId
    ) {

        if (!examId) {

            throw new Error(
                "SyllabusRepository: examId is required."
            );
        }


        const files =
            this.listSyllabusFiles();


        for (
            const file
            of files
        ) {

            const data =
                this.loadFile(
                    path.join(
                        this.rootDir,
                        file
                    )
                );


            if (
                data.examId ===
                examId
            ) {

                return data;
            }
        }


        return null;
    }


    loadAll() {

        return this.listSyllabusFiles()
            .map(
                file =>
                    this.loadFile(
                        path.join(
                            this.rootDir,
                            file
                        )
                    )
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
                `SyllabusRepository: file not found: ${filePath}`
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
