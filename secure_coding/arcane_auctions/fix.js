function sanitize(filter, disallowedKeys = ['password']) {
    const sanitized = JSON.parse(JSON.stringify(filter));
    
    function clean(obj) {
      if (typeof obj !== 'object' || obj === null) return;
      
      if (obj.select && typeof obj.select === 'object') {
        disallowedKeys.forEach(key => {
          if (obj.select.hasOwnProperty(key)) {
            delete obj.select[key];
          }
        });
        
        Object.keys(obj.select).forEach(key => {
          if (typeof obj.select[key] === 'object') {
            clean(obj.select[key]);
          }
        });
      }
      
      if (obj.include && typeof obj.include === 'object') {
        Object.keys(obj.include).forEach(relation => {
          if (!obj.select) obj.select = {};
          obj.select[relation] = obj.select[relation] || { select: {} };
          clean(obj.select[relation]);
        });
        delete obj.include;
      }
      
      Object.keys(obj).forEach(key => {
        if (typeof obj[key] === 'object') {
          clean(obj[key]);
        }
      });
    }
    
    clean(sanitized);
    return sanitized;
}

const filter = req.body.filter || {};
const sanitized_filter = sanitize(filter);
const items = await prisma.item.findMany(sanitized_filter);