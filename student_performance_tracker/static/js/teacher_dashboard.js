// Teacher dashboard behavior (filters, dept dropdown, search)

document.addEventListener('DOMContentLoaded', function () {
  // Department dropdown toggle
  const depToggle = document.getElementById('departmentsToggle');
  const depList = document.getElementById('departmentsList');
  const deptAngle = document.getElementById('deptAngle');

  depToggle?.addEventListener('click', () => {
    if (!depList) return;
    const isHidden = depList.classList.contains('hidden');
    if (isHidden) {
      depList.classList.remove('hidden');
      deptAngle.style.transform = 'rotate(180deg)';
    } else {
      depList.classList.add('hidden');
      deptAngle.style.transform = 'rotate(0deg)';
    }
  });

  // Department buttons both in sidebar and above table
  function filterByDept(dept) {
    const rows = document.querySelectorAll('#studentsTBody tr');
    rows.forEach(r => {
      // expected a data-dept attribute on rows if needed; fallback to server-side filtering
      const rowDept = r.getAttribute('data-dept') || r.querySelector('td:nth-child(2)')?.getAttribute('data-dept') || '';
      if (dept === 'ALL') {
        r.style.display = '';
      } else {
        // fallback: try match using a cell value (if you render data-dept on rows use that first)
        const cellDept = r.getAttribute('data-dept') || r.querySelector('td[data-dept]')?.getAttribute('data-dept') || '';
        if (cellDept) {
          r.style.display = (cellDept === dept) ? '' : 'none';
        } else {
          // if no dept metadata: show all (server-side should filter)
          r.style.display = '';
        }
      }
    });
  }

  document.querySelectorAll('.dept-btn, .filter-btn').forEach(btn => {
    btn.addEventListener('click', () => {
      const dept = btn.getAttribute('data-dept');
      filterByDept(dept);
      // active class
      document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('bg-blue-50', 'dark:bg-blue-900/20'));
      if (btn.classList.contains('filter-btn')) {
        btn.classList.add('bg-blue-50', 'dark:bg-blue-900/20');
      }
    });
  });

  // Search box (client-side)
  const searchInput = document.getElementById('searchInput');
  if (searchInput) {
    searchInput.addEventListener('input', function () {
      const q = this.value.trim().toLowerCase();
      document.querySelectorAll('#studentsTBody tr').forEach(tr => {
        const usn = (tr.querySelector('td:nth-child(1)')?.innerText || '').toLowerCase();
        const name = (tr.querySelector('td:nth-child(2)')?.innerText || '').toLowerCase();
        tr.style.display = (usn.includes(q) || name.includes(q)) ? '' : 'none';
      });
    });
  }
});
