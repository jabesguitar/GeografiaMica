import test from 'node:test';
import assert from 'node:assert/strict';
import { questions, trueFalse, pairs, wordBank } from '../src/questions.js';

test('question bank has 60 complete multiple-choice questions', () => {
  assert.equal(questions.length, 60);
  for (const [i, q] of questions.entries()) {
    assert.ok(q.q, `question ${i} needs a prompt`);
    assert.equal(q.a.length, 4, `question ${i} needs four options`);
    assert.ok(Number.isInteger(q.c) && q.c >= 0 && q.c < 4, `question ${i} has invalid answer index`);
    assert.ok(q.h && q.e, `question ${i} needs a hint and explanation`);
  }
});

test('alternative games have content', () => {
  assert.ok(trueFalse.length >= 10);
  assert.ok(pairs.length >= 10);
  assert.ok(wordBank.length >= 10);
  assert.ok(trueFalse.every(([statement, answer, explanation]) => statement && typeof answer === 'boolean' && explanation));
  assert.ok(pairs.every(([term, definition]) => term && definition));
});
