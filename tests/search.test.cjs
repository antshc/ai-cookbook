'use strict';
const assert = require('node:assert/strict');
const fs = require('node:fs');
const path = require('node:path');
const vm = require('node:vm');
const root = path.resolve(__dirname, '..');
const context = {window:{COOKBOOK:{prefix:'../',problem:'skill-routing'}}, document:{querySelectorAll:()=>[],getElementById:()=>null}, location:{href:'https://example.com/ai-cookbook/problems/skill-routing.html'}, URLSearchParams};
vm.createContext(context);
vm.runInContext(fs.readFileSync(path.join(root,'site/app.js'),'utf8'),context);
const materials = JSON.parse(fs.readFileSync(path.join(root,'dist/search-index.json'),'utf8')).materials;
const state = {q:'',problem:'',artifact:'',task:'',kind:''};
const find = s => materials.filter(m => context.matches(m,{...state,...s}));
assert.equal(find({kind:'recipe'}).length,2);
assert.equal(find({q:'completeness sweep',kind:'recipe'}).length,2);
assert.equal(find({q:'Reconstruct all obligations',kind:'recipe'}).length,1);
assert.equal(find({q:'blocked or partial',kind:'recipe'}).length,1); // full-text body search
assert.ok(find({problem:'skill-routing',artifact:'skill',kind:'source-only'}).length>0);
assert.equal(find({q:'a-phrase-that-does-not-exist'}).length,0);
assert.equal(find({artifact:'template',kind:'recipe'}).length,0);
assert.equal(context.stateFromURL(new URLSearchParams()).problem,'skill-routing');
assert.equal(context.stateFromURL(new URLSearchParams('problem=&q=memory')).problem,''); // cleared chapter survives reload
assert.equal(context.stateFromURL(new URLSearchParams('problem=continuity&kind=recipe')).kind,'recipe');
console.log('Search checks passed: full text, combined filters, empty results and URL state.');
