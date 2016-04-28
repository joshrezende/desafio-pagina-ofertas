var app, base, concat, directory, gulp, gutil, hostname, path, refresh, sass, uglify, imagemin, minifyCSS, del, browserSync, autoprefixer, gulpSequence, shell, sourceMaps, plumber;

gulp        = require('gulp');
gutil       = require('gulp-util');
concat      = require('gulp-concat');
uglify      = require('gulp-uglify');
sass        = require('gulp-sass');
sourceMaps  = require('gulp-sourcemaps');
imagemin    = require('gulp-imagemin');
minifyCSS   = require('gulp-clean-css');
// browserSync = require('browser-sync');
autoprefixer = require('gulp-autoprefixer');
gulpSequence = require('gulp-sequence').use(gulp);
shell       = require('gulp-shell');
plumber     = require('gulp-plumber');

// gulp.task('browserSync', function() {
//     browserSync({
//         server: {
//             baseDir: "static/"
//         },
//         options: {
//             reloadDelay: 250
//         },
//         notify: false
//     });
// });

gulp.task('styles', function() {
    return gulp.src('static/styles/**/*.scss')
                .pipe(plumber({
                  errorHandler: function (err) {
                    console.log(err);
                    this.emit('end');
                  }
                }))
                .pipe(sourceMaps.init())
                .pipe(sass({
                      errLogToConsole: true,
                      includePaths: [
                          'static/styles/**'
                      ]
                }))
                .on('error', gutil.log)
                .pipe(sourceMaps.write())
                .pipe(gulp.dest('static/css'));
});

gulp.task('default', ['styles'], function() {
    gulp.watch('static/styles/**/*.scss', ['styles']);
});
