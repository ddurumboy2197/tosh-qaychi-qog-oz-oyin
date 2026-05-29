**Tosh-qaychi-qog'oz o'yini testlari**

```python
import pytest
from o'yin import ToshQaychiQog'oz

@pytest.fixture
def o'yin():
    return ToshQaychiQog'oz()

def test_tosh_qaychi_qog'oz_qachon_boshlanadi(o'yin):
    assert o'yin.boshlanish_soni == 0

def test_tosh_qaychi_qog'oz_qachon_tosh_kiradi(o'yin):
    o'yin.tosh_kiradi()
    assert o'yin.tosh_soni == 1

def test_tosh_qaychi_qog'oz_qachon_qaychi_kiradi(o'yin):
    o'yin.qaychi_kiradi()
    assert o'yin.qaychi_soni == 1

def test_tosh_qaychi_qog'oz_qachon_qog'oz_kiradi(o'yin):
    o'yin.qog'oz_kiradi()
    assert o'yin.qog'oz_soni == 1

def test_tosh_qaychi_qog'oz_qachon_tosh_qaychi_qog'oz_hisoblanadi(o'yin):
    o'yin.tosh_kiradi()
    o'yin.qaychi_kiradi()
    o'yin.qog'oz_kiradi()
    assert o'yin.hisob == 1

def test_tosh_qaychi_qog'oz_qachon_tosh_qaychi_qog'oz_hisoblanadi_2(o'yin):
    o'yin.tosh_kiradi()
    o'yin.tosh_kiradi()
    o'yin.qaychi_kiradi()
    o'yin.qaychi_kiradi()
    o'yin.qog'oz_kiradi()
    o'yin.qog'oz_kiradi()
    assert o'yin.hisob == 2
```

```javascript
import { describe, it, expect } from 'jest';
import ToshQaychiQog'oz from './o'yin';

describe('Tosh-qaychi-qog\'oz o\'yini', () => {
  let o'yin;

  beforeEach(() => {
    o'yin = new ToshQaychiQog'oz();
  });

  it('qachon boshlanadi', () => {
    expect(o'yin.boshlanish_soni).toBe(0);
  });

  it('qachon tosh kiradi', () => {
    o'yin.tosh_kiradi();
    expect(o'yin.tosh_soni).toBe(1);
  });

  it('qachon qaychi kiradi', () => {
    o'yin.qaychi_kiradi();
    expect(o'yin.qaychi_soni).toBe(1);
  });

  it('qachon qog\'oz kiradi', () => {
    o'yin.qog'oz_kiradi();
    expect(o'yin.qog'oz_soni).toBe(1);
  });

  it('qachon tosh-qaychi-qog\'oz hisoblanadi', () => {
    o'yin.tosh_kiradi();
    o'yin.qaychi_kiradi();
    o'yin.qog'oz_kiradi();
    expect(o'yin.hisob).toBe(1);
  });

  it('qachon tosh-qaychi-qog\'oz hisoblanadi 2', () => {
    o'yin.tosh_kiradi();
    o'yin.tosh_kiradi();
    o'yin.qaychi_kiradi();
    o'yin.qaychi_kiradi();
    o'yin.qog'oz_kiradi();
    o'yin.qog'oz_kiradi();
    expect(o'yin.hisob).toBe(2);
  });
});
```
