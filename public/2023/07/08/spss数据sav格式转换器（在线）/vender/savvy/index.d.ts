import { Display, Scale, Header, Internal, Meta, Parsed, Row, Schema } from './types';
/**
 * An object that stores an {@link ArrayBuffer} and returns subsequent portions on demand
 */
export declare class Feeder {
    private buffer;
    private cursor;
    /**
     *
     * @param buffer An {@link ArrayBuffer} that will be fed out by the object
     */
    constructor(buffer: ArrayBuffer);
    /**
     * Jump the cursor to a position in the buffer.
     * @param position the position in the {@link ArrayBuffer} to jump to
     */
    jump(position: number): void;
    /**
     * Get the next chunk of the ArrayBuffer from the current cursor position
     * and move the cursor.
     * @param size the number of bytes to read from the {@link ArrayBuffer}
     * @returns an {@link ArrayBuffer} of the requested `size` from the cursor position
     */
    next(size: number): ArrayBuffer;
    /**
     * Get the current position of the cursor
     * @returns the current cursor position as a number
     */
    position(): number;
    /**
     * Check whether the {@link ArrayBuffer} has been exhausted
     * @returns a boolean, whether the {@link ArrayBuffer} is exhausted
     */
    done(): boolean;
}
/**
 * A parser for .sav files
 */
export declare class SavParser {
    private decoder;
    private log;
    private readFieldLabel;
    private readFieldMissingCodes;
    private readFieldMissingStrings;
    private readFieldMissingRange;
    private readFieldMissing;
    private readField;
    private getLevel;
    private readScale;
    private readDocument;
    private readSysInteger;
    private readSysFloat;
    private readSysDisplay;
    private readNames;
    private readLongWidths;
    private readLongNames;
    private readUnrecognized;
    private readInternal;
    private readFields;
    /**
     * Create a new parser
     * @param log a string array that will be populated by parse calls
     */
    constructor(log?: Array<string>);
    /**
     * Read the meta fields from a .sav file
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let meta;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.meta(new Feeder(data.buffer)).then(
     *         result => meta = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.meta(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => meta = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const meta;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.meta(new Feeder(buffer))
     *         ).then(
     *             parsed => meta = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with a {@link Meta} object
     */
    meta(feeder: Feeder): Promise<Meta>;
    /**
     * Read the column header fields from a .sav file.
     * Header here refers to the head of the columns of the data, i.e.
     * properties of the variables in the data file
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let headers;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.headers(new Feeder(data.buffer)).then(
     *         result => headers = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.headers(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => headers = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const headers;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.headers(new Feeder(buffer))
     *         ).then(
     *             parsed => headers = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with an Array<{@link Meta}> object
     */
    headers(feeder: Feeder): Promise<Array<Header>>;
    /**
     * Read all schema fields from a .sav file.
     * Schema here refers to all information except for the data cells themselves
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let schema;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.schema(new Feeder(data.buffer)).then(
     *         result => schema = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.schema(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => schema = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const schema;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.schema(new Feeder(buffer))
     *         ).then(
     *             parsed => schema = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with an {@link Schema} object
     */
    schema(feeder: Feeder): Promise<Schema>;
    /**
     * Read all fields from a .sav file.
     * All fields include the full {@link Schema} and all data cells as an
     * Array<{@link Row}.
     * @param feeder A {@link Feeder} object encoding the sav file
     * @remarks
     * From a node.js {@link Buffer} using `fs.readFile`
     * ```
     * fs = require('fs');
     *
     * let all;
     * const parser = new SavParser()
     * // with async readFile
     * fs.readFile('some/path/to/file.sav', (err, data) => {
     *     parser.all(new Feeder(data.buffer)).then(
     *         result => all = result
     *     )
     * });
     * // with syncronous readFileSync
     * parser.all(
     *     new Feeder(fs.readFileSync('/some/path/to/file.sav').buffer)
     * ).then(
     *     parsed => all = parsed
     * );
     * ```
     *
     * In the browser with a File API
     * ```
     *     <input type="file" onchange = "onChange(event)"></input>
     * ```
     * ```
     * const all;
     * function onChange(event){
     *     const file = event.target.files[0];
     *     const reader = new FileReader();
     *     const parser = new SavParser();
     *     reader.onload = function(data){
     *         data.arrayBuffer().then(
     *             buffer => parser.all(new Feeder(buffer))
     *         ).then(
     *             parsed => all = parsed
     *         );
     *     }
     *     reader.readAsArrayBuffer(file);
     * }
     * ```
     * @return A promise resolving with an {@link Parsed} object
     */
    all(feeder: Feeder): Promise<Parsed>;
}
export { Display, Scale, Header, Internal, Meta, Parsed, Row, Schema };
export { Savvy } from './dataset';
