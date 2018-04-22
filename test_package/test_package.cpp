#include <string>
#include "CLI/CLI.hpp"

int main(int argc, char **argv)
{
    CLI::App app("K3Pi goofit fitter");
    app.set_footer("Bincrafters");
    app.set_help_flag("--help", "A help string");
    CLI11_PARSE(app, argc, argv);
}
